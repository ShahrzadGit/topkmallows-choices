#Imports
import math
import numpy as np
from collections import OrderedDict
import matplotlib.pyplot as plt
import sys
from SamplingAlgos import PRIMPOS
from SamplingAlgos import  Find_All_Profiles_Prob
from Aux_funcs import printDP
from Aux_funcs import list_subsets






def dypChip_prob_selected_from_bag(A, S, sigma, n, k, p , beta, w,L):
    
    ell=len(S)
    m=len(L)
    Abar=[a for a in A if a not in sigma]
    r= len(Abar)
   
   # print("bag probablities, n",n,"k",k,"ell",ell, "r",r)
    
    
    val= math.comb(n-k-r, k-ell)/ math.comb(n+1-k, k-ell)
   
    return val

    

def DypChip(A, S, sigma, n, k, p , beta, w,L):
  """
  input parameters:
  A: assortment 
  L: an ordering of elements bar{A} \cup sigma having Abar as the prefix, and sigma in reverse order. 
  sigma: center
  S: profile
  n,k: size of universe and size of top k list
  beta, p, w: TOPKGMM parameters 

  output: vector of size m=len(L) showing the choice probablites of element as ordered in L 
  """

  # check that the paramaters are correct: L,S,sigma, ..
  # print("running DypChip with parameters: n",n, " A",A,"S",S,"sigma",sigma, "k",k)
  ell=len(S)
  m=len(L)
  
  
  # DP table first index presents elements (they are in L), 
  # Second index shows the rank of winner.   Indecies  0,1,..k-1 are used for top k and k is used for bag
  # third index shows iteration of PRIME 0,1,2... ell
  DPtable=np.zeros((m,k+1,ell+1))
  
  # initialize the DPtable by setting the prefix of L 
  ANull=A+[0]
  Abar=[a for a in ANull if a not in sigma]
  r= len(Abar)

  # j shows the position of the winner which can be 0,1,2,.. k-1
  for j in range(k-ell):
    element_sampled_at_j_it=1/(n+1-k-j)
    no_element_sampled_before=1 
    for jp in range(0,j):
       no_element_sampled_before= no_element_sampled_before*(1-(r/(n+1-k-jp))) 
    DPtable[:r,j,0]=  element_sampled_at_j_it*no_element_sampled_before
  winner_from_bag=dypChip_prob_selected_from_bag(A, S, sigma, n, k, p , beta, w,L)
#  print("what we want for bag:",1-np.sum(DPtable[:r,j,0]),"what we get", winner_from_bag)
  DPtable[:r,k,0]= winner_from_bag/r


   # we now start the cases and the recursive constructiono f DP table
      # first sort S w.r.t. sigma:
  index_map = {val: -i for i, val in enumerate(sigma)}
  S_sorted = sorted(S, key=lambda x: index_map[x]) 
  num_sampled_intopk=k-ell
  for q in range(ell):
    table_index=q+1
    a_cur=S_sorted[q] 
    ind_cur=L.index(a_cur)
    num_sampled_intopk=num_sampled_intopk+1
    #case 1:
    
    if a_cur not in ANull:
    #  print("***in case 1*** q is ",q, "a_cur is", a_cur,"index in DPtable:", ind_cur)
      DPtable[ind_cur,:,  table_index]=0
      prev_DP= DPtable[:,: , table_index-1]
      
      for j in range(num_sampled_intopk):
      #  print("we now look at probablities of position",j)
        prob_insertion_after_j=PRIMPOS( S_sorted, sigma, n, k,  beta, w,j+1,None,q) 
     #   print("prob_insert_after j+1",j, "is",prob_insertion_after_j)
        prob_insertion_before_j=PRIMPOS(S, sigma, n, k,  beta, w,0,j,q) 
     #   print("prob_insert_before j",j,"is", prob_insertion_before_j)
        if j>0:
            DPtable[:,j,  table_index]=prev_DP[:,j-1]*prob_insertion_before_j+prev_DP[:,j]*(prob_insertion_after_j)
        if j==0:
            DPtable[:,j,  table_index]=prev_DP[:,j]*(prob_insertion_after_j)
      DPtable[:,k,  table_index]= prev_DP[:,k] 
    #case 2:
    if a_cur in ANull:
    #  print("***in case 2*** q is",q, "a_cur is", a_cur,"index in DPtable:", ind_cur)
      prev_DP= DPtable[:,:,  table_index-1]
      for j in range(num_sampled_intopk):
        insert_prob_after_j=PRIMPOS( S_sorted, sigma, n, k,  beta, w,j+1,None,q)
       # print("prob_insert_after j",j, "is",insert_prob_after_j)
        DPtable[:,j,  table_index]=prev_DP[:,j]*insert_prob_after_j
        insert_prob_at_j=PRIMPOS( S_sorted, sigma, n, k,  beta, w,j,j+1,q) 
        DPtable[ind_cur,j,q+1]=insert_prob_at_j*np.sum(prev_DP[:,j:])
    
  #  print("DP table at iteration q", table_index)
   # printDP(DPtable)
    #print("DP sum",np.sum(DPtable[:,:,table_index] ))
      
    
  #printDP(DPtable)
  #print("DP sum",np.sum(DPtable[:,:,ell] ))
  #print("last table,",DPtable[:,:,ell])
  Ret_vec=np.sum(DPtable[:,:,ell], axis=1)
  return np.squeeze(Ret_vec)

def drop_extras(prob_list,L,ANull):
   notinA=[it for it in L if it not in ANull]
   for it in notinA:
      if not prob_list[L.index(it)]==0:
         print("ERR: element outside A has non-zero probablity")
   ret_dic={k:prob_list[L.index(k)] for k in ANull  }
   return ret_dic
      
   
   
def DyPChIP_final(A,  sigma, n, k, p , beta, w):
   # print("***** starting execution of DypChip with all profiles ******")
    ANull=A+[0]
    Abar=[a for a in ANull if a not in sigma]
    L=Abar+sigma
    profile_ind_range=list(range(2**k))

    # the following line creates two dictionaries, the first one maps i->prob(S)*Z the second one maps i->S, Z is the normalizing constant  
    
    Z,Dic_pr,Dic_sub=Find_All_Profiles_Prob(sigma, n, k, p , beta, w) 
   
   # Apply_DypChip_to_all_profiles=[DypChip(Dic_sub[profile_ind])*Dic_pr(profile_ind)/Z for profile_ind in profile_ind_range ]

    Apply_DypChip_to_all_profiles=[np.array(DypChip(A, Dic_sub[profile_ind], sigma, n, k, p , beta, w,L))*Dic_pr[profile_ind]/Z for profile_ind in profile_ind_range ]

   # for ind in profile_ind_range:
    #   print("index", ind)
     #  print("Dic_pr[profile_ind]/Z",Dic_pr[ind]/Z)
      # print("Dic_sub[profile_ind]",Dic_sub[ind])
       #print("(DypChip(A, Dic_sub[profile_ind], sigma, n, k, p , beta, w,L))",(DypChip(A, Dic_sub[ind], sigma, n, k, p , beta, w,L)))
       #print("final contribution",np.array(DypChip(A, Dic_sub[ind], sigma, n, k, p , beta, w,L))*Dic_pr[ind]/Z)
    prob_list=np.sum( Apply_DypChip_to_all_profiles, axis=0)
   # print("DypCHip results: probs",prob_list,"L",L)
    ret_dic=drop_extras(prob_list,L,ANull)
    return ret_dic

