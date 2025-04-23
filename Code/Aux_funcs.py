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

def find_item_weight(sigma,w,j):
  if j not in sigma:
    print("j not in sigma")
    return None 
  return w[sigma.index(j)+1]

def params_conds(sigma,S,w,n,k):
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






  
    
  

