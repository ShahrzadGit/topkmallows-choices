import math
import numpy as np
from collections import OrderedDict
import matplotlib.pyplot as plt
import sys
import random


from Aux_funcs import list_subsets

# these are the functions we need for sampling (Section 3):


def Profile_probablity(S, sigma, n, k, p ,  w):
# Algorithm 3
# sigma is the center
# n, k , p beta and w are topkGMM's parameters
# w shows the weights of the elements sigma[1],sigma[2],..., sigma[k] and w_perp=w[0]
#  S includes a subset of indices from 1...k, and shows the profile which is sigma(S[1]), sigma(S[2]), \dots sigma(S[\ell])
    if(len(sigma)!=k or len(S)>k) or len(w)!= k+1 or k>n:
        print("wrong parameters")
        return None
    else:
  
        ell=len(S)
        Q_S= (k-ell)*(k-ell-1)/2
        x=0
        y=0
        f_S=w[0]*p*Q_S
        for j in range(k, 0, -1):
            #print("j",j)
            I_sigmaj=k-ell+x
            P_sigmaj=n-2*k+ell+y
           
            if(j in S):
                x=x+1
            else:
                y=y+1
                #print("I_sigmaj", I_sigmaj, "P_sigmaj", P_sigmaj)
                #print("weight of the item:", sigma[j-1],"is", w[j])
                f_S=f_S+w[j]*(I_sigmaj+p*P_sigmaj)
                #print("weighted sum of inversions:", I_sigmaj+p*P_sigmaj)
        return f_S


    
def Find_Z(S, sigma, n, k,   w,beta):
    #finds Z(S) as defined in Lemma 3.3
    if(len(sigma)!=k or len(S)>k) or len(w)!= k+1 or k>n:
        print("wrong parameters")
        return None
    else:
        ell=len(S)

        first_term=1
        for i in range(k-ell):
            first_term=first_term*(n-2*k+ell+1+i)
     #   print("first term", first_term)
        second_term=1
        for j in range(ell):
            sum_j=0
            for r in range(k-j):
                new_term=np.exp(-beta*w[S[j]]*r)
              #  print("prod_ex, s_j:",S[j], new_term)
                sum_j=sum_j+new_term
            
            second_term=second_term*sum_j
        return first_term*second_term
    

def Find_All_Profiles_Prob(sigma, n, k, p , beta, w):
  
# creates two dictionaries, the first one maps i->prob(S)*Z the second one maps i->S 
# calculates normalizing constant Z
# together the two dictionaries can be used to find the probablity of all profiles. 

  profile_list=list_subsets(k)
  counter=0
  Z=0
  Dic_pr={}
  Dic_sub={}
  for S in profile_list:
    f_S=Profile_probablity(S, sigma, n, k, p ,  w)
    print("f_S",S, f_S)
    Z_S=Find_Z(S, sigma, n, k,   w,beta)
    print("Z_S",S, Z_S)
    pr=np.exp(-beta*f_S)*Z_S
     
    Dic_pr[counter]=pr
    Dic_sub[counter]=S
    print("Z and Pr",Z,pr)
    Z=Z+pr
    counter=counter+1
  return Z,Dic_pr,Dic_sub

def PRIME(S, sigma, n, k,  beta, w):
    N=list(range(1,n+1))
    ell=len(S)
    tau=[]
    bag=[i for i in  N if i not in sigma]
    
   
    for j in range(k-ell):
    
        r=random.choice(bag)
        bag.remove(r)
        tau.insert(0,r)
    index_range=list(range(k-ell+1))
    cur_ind=ell -1
    print("bag part is sampled in tau", tau)
    
    Z=0
    for j in range(ell):
        print("index_range", index_range, "s_",cur_ind,"is", S[cur_ind])
        cur_w=w[S[cur_ind]]

        probs=[np.exp(-beta*cur_w*j) for j in index_range]
      
        print("probs", probs)
        random_ind=random.choices(index_range,probs)[0]
        tau.insert(random_ind,S[cur_ind])
        print("tau",tau)
        cur_ind=cur_ind-1
        print("cur_ind",cur_ind)
    return tau



    









def generate_sample(sigma, n, k,p,  beta, w, dic_pr, dic_sub,Z):
 #    Z,Dic_pr,Dic_sub=(sigma, n, k, p , beta, w)
    probs=dic_pr.values()
    ind_range=list(range(2^k))
    S_ind=random.choices(ind_range,probs)[0]
    S=dic_sub[S_ind]
    tau=PRIME(S, sigma, n, k,  beta, w)

    return tau 
                       


#test files:
    
def test_alg3():
        # example 1 center identity 
    print("Hello! testing profile_probablity")
    sigma=[1,2,3,4,5]
    w=[2,1,1,1,1,1]
    n=11
    k=5
    p=1
    S=[2,4]
    f=Profile_probablity(S, sigma, n, k, p ,  w)
    print("f",f)
    # expected result: 
    # I_5=3, P_5=3
    # I_3=4, P_3=4
    # I_1=5, P_1=5
    # f=6+8+10+6=30

    sigma=[1,2,3,4,5,6]
    w=[2,1,1,1,1,1,1]
    n=20
    k=6
    p=1
    p=1/2
    S=[2,3,6]
    f=Profile_probablity(S, sigma, n, k, p ,  w)
    print("f",f)

    # expected result: 
    # I_5=4, P_5=11
    # I_3=4, P_3=12
    # I_1=6, P_1=13
    # for p=1  f=15+16+19+2*3=56
    # for p=1/2   f=9.5+10+12.5+2*1.5=35


    # example 2 center is non-identity 

    sigma=[2,5,3,4,8,9]
    w=[1,2,3,4,5,6,7]
    n=16
    k=6
    p=1
    #p=1/2
    S=[2,5]
    # which means the profile is sigma[2]=3 and sigma[5]=9 
    f=Profile_probablity(S, sigma, n, k, p ,  w)
    print("f",f)

def test_findZ():
    print("Hello! testing find Z")
    sigma=[1,2,3,4,5]
    w=[2,1,1,1,1,1]
    n=10
    k=5
    p=1
    beta=1
    S=[2,4]
    Z_S=Find_Z(S, sigma, n, k,   w,beta)
    print("Z_S",Z_S)
    # expected result: 60*(1+e^-1+e^-2+e^-3+e^-4)*(1+e^-1+e^-2+e^-3)=146.415

    w=[2,1,2,1,1,1]
    Z_S=Find_Z(S, sigma, n, k,   w,beta)
    print("Z_S",Z_S)
    # expected result: 60*(1+e^-2+e^-4+e^-6+e^-8)*(1+e^-1+e^-2+e^-3)=

    S=[2,4,5]
    Z_S=Find_Z(S, sigma, n, k,   w,beta)
    print("Z_S",Z_S)
    # expected result: 20*(1+e^-2+e^-4+e^-6+e^-8)*(1+e^-1+e^-2+e^-3)*(1+e^-1+e^-2)= 53.99

    S=[]
    Z_S=Find_Z(S, sigma, n, k,   w,beta)
    print("Z_S",Z_S)
    # expected result: 120


def test_all_prof_prob():
    print("Hello, I am testing Find_All_Profiles_Prob")
    sigma=[1,2,3]
    k=3
    n=10
    w=[2,1,1,1]
    beta=1
    p=1
    Find_All_Profiles_Prob(sigma, n, k, p , beta, w)

def test_PRIME():
    print("testing PRIME")
    sigma=[1,2,3,4,5]
    w=[2,1,1,1,1,1]
    n=10
    k=5
    p=1
    beta=1
    S=[2,4]
    PRIME(S, sigma, n, k,  beta, w)




test_PRIME()