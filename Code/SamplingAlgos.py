import math
import numpy as np
from collections import OrderedDict
import matplotlib.pyplot as plt
import sys
import random
from Aux_funcs import find_item_weight
from Aux_funcs import list_subsets
from Aux_funcs import params_conds
"""
 list of algorithms:

 Profile_probablity(S, sigma, n, k, p ,  w)
 Find_Z(S, sigma, n, k ,w, beta)
 Find_All_Profiles_Prob(sigma, n, k, p , beta, w)
 PRIME(S, sigma, n, k,  beta, w)
 generate_sample(sigma, n, k,p,  beta, w, dic_pr, dic_sub,Z)
------------------
parameters: 
n, k , p beta and w are topkGMM's parameters,
S is a profile
------------------
n,k integers
p float 
sigma is the center and a subset of 1,2,...n: it is a list. The identity is sigma(i)=i+1
w is a list. It shows the weights of the elements in the center and w_0 as  w_{sigma_i}=w[i], w_perp=w[0]: 
S denotes a profile. It must be a list and a subset of sigma


"""
# these are the functions we need for sampling (Section 3):


def Profile_probablity(S, sigma, n, k, p ,  w):
# Algorithm 4
# sigma is the center
# n, k , p beta and w are topkGMM's parameters
# w shows the weights of the elements sigma[1],sigma[2],..., sigma[k] and w_perp=w[0]
# S includes a subset of sigma
    if (not params_conds(sigma,S,w,n,k)):
        print("wrong parameters")
        return None
    else:
      #  print("profile probablity of ",S)
  
        ell=len(S)
        Q_S= (k-ell)*(k-ell-1)/2
        x=0
        y=0
        f_S=w[0]*p*Q_S
        for j in range(k, 0, -1):
           # print("j",j)
          #  print("sigma j", sigma[j-1])
            I_sigmaj=k-ell+x
            P_sigmaj=n-2*k+ell+y
           
            if(sigma[j-1] in S):
                x=x+1
               
            else:
                y=y+1
              #  print("I_sigmaj", I_sigmaj, "P_sigmaj", P_sigmaj)
              #  print("weight of the item:", sigma[j-1],"is", w[j])
                f_S=f_S+find_item_weight(sigma,w,sigma[j-1])*(I_sigmaj+p*P_sigmaj)
               # print("weighted sum of inversions:", I_sigmaj+p*P_sigmaj)
        return f_S


    
def Find_Z(S, sigma, n, k,   w,beta):
    #finds Z(S) as defined in Lemma 3.3
    if(not params_conds(sigma,S,w,n,k)):
        print("wrong parameters")
        return None
    else:
        ell=len(S)

        first_term=1
        for i in range(k-ell):
            first_term=first_term*(n-2*k+ell+1+i)
     #  print("first term", first_term)
        second_term=1
        for j in range(ell):
            sum_j=0
            for r in range(k-j):
                new_term=np.exp(-beta*find_item_weight(sigma,w,S[j])*r)
              #  print("prod_ex, s_j:",S[j], new_term)
                sum_j=sum_j+new_term
            
            second_term=second_term*sum_j
        return first_term*second_term
    

def Find_All_Profiles_Prob(sigma, n, k, p , beta, w):
  
# creates two dictionaries, the first one maps i->prob(S)*Z the second one maps i->S 
# calculates normalizing constant Z
# together the two dictionaries can be used to find the probablity of all profiles. 

  profile_list=list_subsets(sigma)
  counter=0
  Z=0
  Dic_pr={}
  Dic_sub={}
  for S in profile_list:
    f_S=Profile_probablity(S, sigma, n, k, p ,  w)
  #  print("f_S",S, f_S)
    Z_S=Find_Z(S, sigma, n, k,   w,beta)
   # print("Z_S",S, Z_S)
    pr=np.exp(-beta*f_S)*Z_S
     
    Dic_pr[counter]=pr
    Dic_sub[counter]=S
   # print("Z and Pr",Z,pr)
    Z=Z+pr
    counter=counter+1
  return Z,Dic_pr,Dic_sub

def PRIME(S, sigma, n, k,  beta, w):
    if (not params_conds):
        return None 
    N=list(range(1,n+1))
    ell=len(S)
    tau=[]
    bag=[i for i in  N if i not in sigma]
    for j in range(k-ell):  
        r=random.choice(bag)
        bag.remove(r)
        tau.insert(0,r)
    index_range=list(range(k-ell))
   # print("k-ell and index range", k-ell, index_range)
    cur_ind=ell -1
    #print("bag part is now sampled in tau", tau)
    
    Z=0
    for j in range(ell):
        index_range=index_range+[k-ell+j]
      #  print("index_range", index_range, "s_",cur_ind,"is", S[cur_ind])
        cur_w=find_item_weight(sigma,w,S[cur_ind])
        probs=[np.exp(-beta*cur_w*j) for j in index_range]

      #  print("probs", probs)
        random_ind=random.choices(index_range,probs)[0]
     #   print("random_ind",random_ind)
        tau.insert(random_ind,S[cur_ind])
      
       # print("tau",tau)
        cur_ind=cur_ind-1
       
    return tau




def generate_sample(sigma, n, k,p,  beta, w, dic_pr, dic_sub,Z):
 #    Z,Dic_pr,Dic_sub=(sigma, n, k, p , beta, w)
    if (not params_conds):
        return None
    probs=list(dic_pr.values())
    #print("probs", probs)
    ind_range=list(range(2**k))
    #print("ind_range",ind_range)
    S_ind=random.choices(ind_range,probs)[0]
    S=dic_sub[S_ind]
   # print("S,S_ind", S,S_ind)
    tau=PRIME(S, sigma, n, k,  beta, w)

    return tau 
                       


