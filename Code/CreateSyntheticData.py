from Aux_funcs import list_subsets
from Aux_funcs import gen_rand_assortment
from SamplingAlgos import Profile_probablity
from SamplingAlgos import  Find_Z
from SamplingAlgos import  Find_All_Profiles_Prob
from SamplingAlgos import PRIME
from SamplingAlgos import generate_sample
from Aux_funcs import find_item_weight
from LearningAlgos import LearnTopElement
import random
import matplotlib.pyplot as plt
import numpy as np


def TopAssElement(tau,A):
    for i in tau:
        if i in A:
            return i
    return None 


def Choice(A, tau,n):

    N=list(range(1,n+1))
    if ( not set(A)<= set(N)):
        print("A must be subset of 1,2,..n")
        return None
    Anull=A+[0]
    Nnull=N+[0]
    if ( not set(tau)<= set(Nnull)):
        print("tau must be subset of 0,1,2,..n")
        return None
    k=len(tau)
    for i in range(k):
        if tau[i] in Anull:
            return tau[i]
      
    
   
    c=random.choice(Anull)
    return c

    





def CreateChoiceSamples(m, sigma, w, beta, n, k,p, A):
    # create m samples from a distibution diven the other parameters
    # m top-k samples are stored in T
    # choices w.r.t. A are stored in S
    T=[]
    S=[]

    Z,Dic_pr,Dic_sub=Find_All_Profiles_Prob(sigma, n, k, p , beta, w)
    for i in range(m):
        tau=generate_sample(sigma, n, k,p,  beta, w, Dic_pr, Dic_sub,Z)
        T=T+[tau]
        S=S+[Choice(A,tau,n)]
    return T,S


def find_accuracy_learningtop(n,k,r,m,beta, p,num_runs):



   
    N=list(range(1,n+1))

    sigma=list(range(1,k+1))
    w=[2]+([1]*(k))
    print("parameters are: n",n, "sigma", sigma, "w", w )
    
    Acclist=[]
    for j in range(10):
        acc=0
        for i in range(num_runs):
        # we sample the assortment such that: k/2 elements are from sigma, and the rest can be anywhere between 1...n
            s=int(r/2)+1
            A=gen_rand_assortment(sigma,N,s,r-s)
            print("sampled assortment:",A)
        # we now create m samples and store them list S (top-k samples), and T (choices)
            T,S=CreateChoiceSamples(m, sigma, w, beta, n, k,p, A)
       # print("T",T)
       # print("S",S)

        # learn the top element:
            x=LearnTopElement(A,S)
            y=TopAssElement(sigma,A)
            print("learned: ",x," real: ",y)
            if x==y:
                acc=acc+1
            
          
        Acclist=Acclist+[acc/num_runs]
        print("Acclist",Acclist)
    return np.mean(Acclist),np.std(Acclist)




def exp1(n,k,r,beta, p):
    num_runs=10
    Accuracylistmean=[]
    Accuracyliststd=[]
    for i in range(1,51):
        m=i*10
        accmean,accstd=find_accuracy_learningtop(n,k,r,m,beta, p,num_runs)
        Accuracylistmean=Accuracylistmean+[accmean]
        Accuracyliststd=Accuracyliststd+[accstd]
    return Accuracylistmean,Accuracyliststd

n=100
k=10
r=8
beta=0.4
p=0.5
Ly,Lv=exp1(n,k,r,beta, p)


x = np.array(range(10, 510,10))
y_beta4 = np.array(Ly)
v= np.array(Lv)
plt.errorbar(x, y_beta4, v, fmt='o-', capsize=5,color="blue",label="beta=0.4")

beta=0.6
Ly,Lv=exp1(n,k,r,beta, p)
y_beta6 = np.array(Ly)
v= np.array(Lv)
plt.errorbar(x, y_beta6, v, fmt='o-', capsize=5,color="red",label="beta=0.6")

beta=0.8
Ly,Lv=exp1(n,k,r,beta, p)
y_beta8 = np.array(Ly)
v= np.array(Lv)
plt.errorbar(x, y_beta8, v, fmt='o-', capsize=5, color="orange",label="beta=0.8")

beta=1
Ly,Lv=exp1(n,k,r,beta, p)
y_beta1 = np.array(Ly)
v= np.array(Lv)
plt.errorbar(x, y_beta1, v, fmt='o-', capsize=5,color="green",label="beta=1")

beta=1.2
Ly,Lv=exp1(n,k,r,beta, p)
y_beta12 = np.array(Ly)
v= np.array(Lv)
plt.errorbar(x, y_beta1, v, fmt='o-', capsize=5,color="brown",label="beta=1.2")

plt.xlabel("number of samples")
plt.ylabel("accuracy")
plt.legend()

file_path = f"/Users/sh1678/Dropbox/Research/Mallows/topkmallows-choices/Plots/beta: 0.4-1.2_n{n}_k{k}_r{r}_p{p}.png"

plt.savefig(file_path)



    