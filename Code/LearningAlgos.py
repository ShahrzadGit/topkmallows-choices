
import random 
import numpy as np 



"""
List of algorithms:

* Choice(A, tau,n) returns choice of tau from assortment A

* LearnTopElement(A,C) implementation of FindTop algorithm. 

* BuCchoi(N,S) implementation of BuCchoi-II algorithm. S is a sample set including top-k lists which represent preferences of customers. We assume the prefrences are sampled 
From a TOPKGMM


List of common parameters:
tau: top k list, we assumed it is a customer prefrence sampled from a TOPKGMM
n is the number of items 
A: is a list, it shows the assortment; A should always be a subset of 1....n
C: choice data 
We always show the no choice option with 0

"""

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


def LearnTopElement(A,C):
    # Algorithm 3
    # A is the assortment 
    # C is a set of choice samples 
    # two dimensional array X is filled so that at the end of the for loop we have:
    # X_ij= # samples in which  A[i] was chosen and A[j] was not, we let A[r]=Null which is A[r]=0 
    # count_per_item is later used for breaking ties. 

    r=len(A)
    A=A+[0]
    X=[[0 for i in range(r+1)] for j in range(r+1)]
    for c in C:
        i=A.index(c)
        for j in range(r+1):
            if j !=i:
                X[i][j]=X[i][j]+1
                X[j][i]=X[j][i]-1
              #  print("incremented X",i,j, "because choice is",c)
    m=len(C)
   # print("X",X)
    Y=np.array(X)/m         #Y=[[X[i][j]/m for i in range(r+1)] for j in range(r+1)]
    #print("Y",Y)
    count_mat = Y 
    count_per_item = np.sum(count_mat >= 1/(2*(r+1)), axis = 1)
 #   print("count per item,", count_per_item)
    max_item_index = np.argmax(count_per_item)
    if count_per_item[max_item_index] >= r:
      most_wanted_item = A[max_item_index]
    else:
      most_wanted_item = None

    return most_wanted_item, count_per_item
 

    
def break_ties_and_make_list(sigma_dic,scores_to_break_ties):

    # runtime is n^2; n being size of sigma_dic
    max_rank = max(sigma_dic.values())
    sigma_list=[]
    for i in range(max_rank+1):
        
        for it, it_rank in sigma_dic.items():
            L=[]
            if it_rank ==i: 
                L=L+[it]
             #   print("all elements ranked", it_rank, "are", L)
            sorted_L = sorted(L, key=lambda x: scores_to_break_ties[x])
            sigma_list=sigma_list+sorted_L

    return sigma_list 






    
def BuCchoi(N,S):
    n=len(N)
    T=[]
    scores_to_break_ties={key: 0 for key in N}
    for i in N:
        A=[i]
        C=[]
        for tau in S:
            c=Choice(A, tau,n)
            C=C+[c]
        top, scores=LearnTopElement(A,C)
     #   print("learned element, A=",A ,"is",top)
        if top!=None and top not in T and top!=0:
            T=T+[top]
            scores_to_break_ties[top]=scores_to_break_ties[top]+scores[A.index(top)]
     # sigma_dic maps each element in T to its learned rank
    sigma_dic={}
   # print("sigma",sigma)
   # print("learned top elements",T)
    for i in T:
        l=0
        for j in T:
            if j!=i:
                A=[i,j]
                C=[]
                for tau in S:
                  c=Choice(A, tau,n)
                  C=C+[c]
                top,scores=LearnTopElement(A,C)
                if top==j:
                    l=l+1
       # print("i,l",i,l)
        sigma_dic[i]=l
     

    sigma_list=break_ties_and_make_list(sigma_dic,scores_to_break_ties)
  

    return sigma_dic, sigma_list 




        

        


