import math
import numpy as np
from collections import OrderedDict
import matplotlib.pyplot as plt

import sys
import random



def list_subsets(sigma):
  k=len(sigma)
  L=[[]]
  for i in sigma:
    l_new=[]
    for l in L:
      l_new=l_new+[l+[i]]
    L=L+l_new
  return L

def find_item_weight(sigma,w,el):
  # find the weight of an item el: w_ell for instance if sigma=[3,6,7,1] and w=[1,2,3,4,5] then the weight of 7 is 4 and the weight of 1 is 5
  if el not in sigma:
    print("element not in sigma")
    return None 
  return w[sigma.index(el)+1]

def params_conds(sigma,S,w,n,k):
  """
  sigma: center
  S: profile 
  w: vector of weights 
  """
  N=list(range(1,n+1))
  if not set(S)<=set(sigma):
    print("Err: S should be subset of sigma")
    return False
  if not set(sigma)<=set(N):
    print("Err: sigma should be subset of N")
    return False 
  if not len(w)==(len(sigma)+1):
    print("Err: w should be of size k+1; k is the size of sigma")
    return False 
  if not len(sigma)==k:
    print("Err: k is the lenght of w")
    return False 
  return True 

def gen_rand_assortment(sigma,N,r1,r2):
  # samples r1 elements from sigma and r2 from N (no duplicate)
  A=[]
  while len(A)<r1:
    rand=random.choice(sigma)
    if rand not in A:
      A=A+[rand]
  while len(A)<r1+r2:
    rand=random.choice(N)
    if rand not in A:
      A=A+[rand]
  return A

def compare(dic_sigma,i,j):
  # returns the higher element between i and j w.r.t. sigma
  # returns none if they are parallel, i.e., both in bag
  topsigma=list(dic_sigma.keys())
  if i in  topsigma and j in topsigma:
    if dic_sigma[i]<dic_sigma[j]:
      return i
    else:
      return j
  if i not in topsigma and j not in topsigma:
    return None
  if i in topsigma:
    return i
  if j in topsigma:
    return j


def make_list_dic(sigma):
  dic_sigma={}
  for i in range(len(sigma)):
    dic_sigma[sigma[i]]=i
  return dic_sigma


def distance(dic_tau,dic_sigma,p):
  inv=0
  invp=0
  topsigma=list(dic_sigma.keys())
  toptau=list(dic_tau.keys())
  for i in range(len(topsigma)):
    for j in topsigma[i+1:]:
      if compare(dic_tau,topsigma[i],j)==None:
        invp=invp+1
      else:
        if compare(dic_tau,topsigma[i],j)!=compare(dic_sigma,topsigma[i],j):
          inv=inv+1
  for i in range(len(toptau)):
    for j in toptau[i+1:]:
      if compare(dic_sigma,toptau[i],j)==None:
        invp=invp+1

    
       

  return inv+invp*p

def printDP(L):
  n=len(L)
  for i in range(n):
    print("array number", i)
    print(L[i])



      
    





  
    
  

