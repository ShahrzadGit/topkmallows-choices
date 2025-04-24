




"""
List of algorithms:




List of common parameters:
n is the number of items 
A: is a list, it shows the assortment; A should always be a subset of 1....n
We always show the no choice option with 0

"""


def LearnTopElement(A,S):
    # Algorithm 3
    # A is the assortment 
    # S is a set of choice samples 
    # two dimensional array X is filled so that at the end of the for loop we have:
    # X_ij= # samples in which  A[i] was chosen and A[j] was not, we let A[r]=Null which is A[r]=0 
    
    r=len(A)
    A=A+[0]
    X=[[0 for i in range(r+1)] for j in range(r+1)]
    for c in S:
        i=A.index(c)
        for j in range(r+1):
            if j !=i:
                X[j][i]=X[j][i]+1
                X[i][j]=X[i][j]-1
              #  print("incremented X",i,j, "because choide is",c)
    m=len(S)
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


