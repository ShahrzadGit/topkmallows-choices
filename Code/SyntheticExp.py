from Aux_funcs import list_subsets
from Aux_funcs import gen_rand_assortment
from SamplingAlgos import Profile_probablity
from SamplingAlgos import  Find_Z
from SamplingAlgos import  Find_All_Profiles_Prob
from SamplingAlgos import PRIME
from SamplingAlgos import generate_sample
from Aux_funcs import find_item_weight
from LearningAlgos import LearnTopElement
from LearningAlgos import Choice
from LearningAlgos import BuCchoi
from Aux_funcs import distance
from Aux_funcs import make_list_dic
import random
import numpy as np
import sys
import time
from DyPChiP import DyPChIP_final
import math


def TopAssElement(tau,A):
    for i in tau:
        if i in A:
            return i
    return None 



def CreateSamples(m, sigma, w, beta, n, k,p, Dic_pr, Dic_sub,Z):
    # create m samples from a distibution diven the other parameters
    # m top-k samples are stored in T
    
    T=[] 
    for i in range(m):       
        tau=generate_sample(sigma, n, k,p,  beta, w, Dic_pr, Dic_sub,Z)   
        T=T+[tau]
     
    
    return T
    





def CreateChoiceSamples(m, sigma, w, beta, n, k,p, A,Dic_pr, Dic_sub,Z):
    # create m samples from a distibution diven the other parameters
    # m top-k samples are stored in T
    # choices w.r.t. A are stored in S
    T=[]
    S=[]
    
    exc_time=[]
    for i in range(m):
        start=time.time()
        tau=generate_sample(sigma, n, k,p,  beta, w, Dic_pr, Dic_sub,Z)
        end=time.time()
        exc_time=exc_time+[end-start]
        T=T+[tau]
        S=S+[Choice(A,tau,n)]
    end=time.time()
    exc_time_per_sample=np.mean(exc_time)
    return T,S,  exc_time_per_sample


def find_accuracy_learningtop(n,k,w,r,m,beta, p,num_runs):

    N=list(range(1,n+1))
    sigma=list(range(1,k+1))

    # run the preprocessing step for sampling 
    start=time.time()
    Z,Dic_pr,Dic_sub=Find_All_Profiles_Prob(sigma, n, k, p , beta, w)
    end=time.time()
    preprocessing_time=end-start
    print("preprocessing time for sampling:",  preprocessing_time )
    
    #print("parameters are: n",n, "sigma", sigma, "w", w, "beta", beta )
    
    Acclist=[]
    sample_exc_time=[]
    for j in range(10):
        acc=0
        for i in range(num_runs):
        # we sample the assortment such that: k/2 elements are from sigma, and the rest can be anywhere between 1...n
            s=int(r/2)+1
            A=gen_rand_assortment(sigma,N,s,r-s)
          #  print("sampled assortment:",A)
        # we now create m samples and store them list T (top-k samples), and S (choices)
            T,S, exc_time_per_sample=CreateChoiceSamples(m, sigma, w, beta, n, k,p, A,Dic_pr, Dic_sub,Z)
            sample_exc_time= sample_exc_time+[exc_time_per_sample]
          #  print("T",T)
           # print("S",S)

        # learn the top element:
            x, count_per_item=LearnTopElement(A,S)
            y=TopAssElement(sigma,A)
           # print("learned: ",x," real: ",y)
            if x==y:
                acc=acc+1
            
          
        Acclist=Acclist+[acc/num_runs]
    print("amortized time for sample size ", m, "is: ", np.mean(sample_exc_time))
   # print("Acclist",Acclist)
    return np.mean(Acclist),np.std(Acclist)

def Find_Bucchoi_Accuracy(n,sigma,w,m,beta, p,num_runs):
    real_center=make_list_dic(sigma)
    N=list(range(1,n+1))
    if not set(sigma)<=set(N):
        print("sigma should be subset of 1..n")
        return None
    k=len(sigma)
    Z,Dic_pr,Dic_sub=Find_All_Profiles_Prob(sigma, n, k, p , beta, w)
    sigmalist=[]
    distancelist=[]
    for j in range(num_runs):
        T=CreateSamples(m, sigma, w, beta, n, k,p, Dic_pr, Dic_sub,Z)
        #print("round,",j,"samples:",T)
        learned_center,center_l=BuCchoi(N,T)
       # print("learned_dic:", learned_center)
       # print("learned_list:", center_l)
        sigmalist=sigmalist+[learned_center]
        distancelist=distancelist+[distance(learned_center,real_center,p)]
    return sigmalist,distancelist





def exp1(n,k,w,r,beta, p):
    num_runs=10
    Accuracylistmean=[]
    Accuracyliststd=[]
    for i in range(1,51):
        m=i*5
        accmean,accstd=find_accuracy_learningtop(n,k,w,r,m,beta, p,num_runs)
        Accuracylistmean=Accuracylistmean+[accmean]
        Accuracyliststd=Accuracyliststd+[accstd]
    return Accuracylistmean,Accuracyliststd


def exp2(n,sigma,w,beta, p):
    num_runs=10
    distancelistmean=[]
    distanceliststd=[]
   
    #sample_sizes=[20*i for i in range(2,15)]
    sample_sizes=[100,200]
    for m in sample_sizes:
        
        sigmalist,distancelist=Find_Bucchoi_Accuracy(n,sigma,w,m,beta, p,num_runs)
        distancelistmean=distancelistmean+[np.mean(distancelist)]
        distanceliststd=distanceliststd+[np.std(distancelist)]

    #print("results:",sigmalist,distancelist)
    return distancelistmean, distanceliststd

def exp3(n,sigma,k,w,beta, p,m,A):
    # this experiment tests DypChip

    # first we create m samples and count the frequency that each element in ANull wins

    Z,dic_pr,dic_sub=Find_All_Profiles_Prob(sigma, n, k, p , beta, w)
    ANull=A+[0]
    countdic={key: 0 for key in ANull}
    for i in range(m):
        tau=generate_sample(sigma, n, k,p,  beta, w, dic_pr, dic_sub,Z)
        c=Choice(A, tau,n)
        countdic[c]=countdic[c]+1

    # we now run DypChip
    start=time.time()
    Ret_dic=DyPChIP_final(A,  sigma, n, k, p , beta, w)
    end=time.time()
    
    errdic={key: None for key in ANull}
    for item in ANull:
        imp_val=countdic[item]/m 
        dypchip_val=Ret_dic[item]
        errdic[item]= abs(imp_val-dypchip_val)

    #print(errdic)
    vec_err=list(errdic.values())
    dypchip_runtime=end-start
 #   return np.mean(vec_err), np.std(vec_err), dypchip_runtime
    return vec_err
def exp4(n):
    # for various k and r
    beta=0.6
    p=0.5
    runtimes=[]
    k_range=[4,6,8,10,12,14,16,18,20]
    print(k_range)
    for k in k_range:
        sigma=list(range(1,k+1))
        w=[1 for i in sigma]
        w=w+[1]
        A=list(range(1,k-7))+[17,18]
        start=time.time()
        Ret=DyPChIP_final(A,  sigma, n, k, p , beta, w)
        end=time.time()
        runtimes= runtimes+[end-start]
    return runtimes



