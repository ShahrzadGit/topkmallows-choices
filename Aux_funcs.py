import math
import numpy as np
from collections import OrderedDict
import matplotlib.pyplot as plt
import sys



def list_subsets(k):
  L=[[]]
  for i in range(k):
    l_new=[]
    for l in L:
      l_new=l_new+[l+[i]]
    L=L+l_new
  return L