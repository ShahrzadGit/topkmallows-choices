
import random 



"""
List of algorithms:




List of common parameters:
n is the number of items 
A: is a list, it shows the assortment; A should always be a subset of 1....n
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
    
    r=len(A)
    A=A+[0]
    X=[[0 for i in range(r+1)] for j in range(r+1)]
    for c in C:
        i=A.index(c)
        for j in range(r+1):
            if j !=i:
                X[j][i]=X[j][i]+1
                X[i][j]=X[i][j]-1
              #  print("incremented X",i,j, "because choide is",c)
    m=len(C)
   # print("X",X)
    Y=[[X[i][j]/m for i in range(r+1)] for j in range(r+1)]
    #print("Y",Y)
    T=[None]*(r+1)
    for i in range(r+1):
        count=0
        for j in range(r+1):
            if Y[i][j]>1/(2*(r+1)):
                count=count+1
        T[i]=count
   # print("all counts:",T)

    if T.count(r)==1:
        return A[T.index(r)]
    if T.count(r)==0:
        return None
    else: 
        "print multiple elements have been found"
        return None 
    
def BuCchoi(N,S):
    n=len(N)
    T=[]
    for i in N:
        A=[i]
        C=[]
        for tau in S:
            c=Choice(A, tau,n)
            C=C+[c]
        top=LearnTopElement(A,C)
     #   print("learned element, A=",A ,"is",top)
        if top!=None and top not in T and top!=0:
            T=T+[top]
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
                top=LearnTopElement(A,C)
                if top==j:
                    l=l+1
       # print("i,l",i,l)
        sigma_dic[i]=l

    return sigma_dic




        

        


