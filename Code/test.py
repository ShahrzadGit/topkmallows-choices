from Aux_funcs import list_subsets
from SamplingAlgos import Profile_probablity
from SamplingAlgos import  Find_Z
from SamplingAlgos import  Find_All_Profiles_Prob
from SamplingAlgos import PRIME
from SamplingAlgos import generate_sample
from Aux_funcs import find_item_weight
from LearningAlgos import LearnTopElement
from Aux_funcs import compare
from Aux_funcs import distance
from Aux_funcs import make_list_dic
from CreateSyntheticData import Choice
from CreateSyntheticData import CreateChoiceSamples



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
    Z,Dic_pr,Dic_sub=Find_All_Profiles_Prob(sigma, n, k, p , beta, w)
    print("Dic_pr", Dic_pr)
    print("Dic_sub", Dic_sub)

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
    sigma=[2,4,5,6,8]
    w=[2,1,1,1,1,1]
    n=10
    k=5
    p=1
    beta=1
    S=[2,8]
    PRIME(S, sigma, n, k,  beta, w)

def test_list_subsets():
    sigma=[1,2,3,4]
    print(list_subsets(sigma))
    sigma=[3,5,6,7]
    print(list_subsets(sigma))
    sigma=[3,5,7]
    print(list_subsets(sigma))
def test_find_item_weight():
    sigma=[2,3,7]
    w=[1,3,4,10]
    j=7
    print(find_item_weight(sigma,w,j))
    j=8
    print(find_item_weight(sigma,w,j))

def test_gen_sample():
    sigma=[1,2,3]
    k=3
    n=10
    w=[2,1,1,1]
    beta=1
    p=1
    print("testing test_get_sample, param: sigma,",sigma, "n", n, "beta,", beta, "k", k  )
    Z,Dic_pr,Dic_sub=Find_All_Profiles_Prob(sigma, n, k, p , beta, w)
    for i in range(10):
        print("sample", i)
        tau=generate_sample(sigma, n, k,p,  beta, w, Dic_pr, Dic_sub,Z)
        print("sample", i, ":",tau)
    beta=0.5
    print("testing test_get_sample, param: sigma,",sigma, "n", n, "beta,", beta, "k", k  )

    Z,Dic_pr,Dic_sub=Find_All_Profiles_Prob(sigma, n, k, p , beta, w)
    for i in range(20):
        print("sample", i)
        tau=generate_sample(sigma, n, k,p,  beta, w, Dic_pr, Dic_sub,Z)
        print("sample", i, ":",tau)
    sigma=[5,2,7]

    print("testing test_get_sample, param: sigma,",sigma, "n", n, "beta,", beta, "k", k  )

    Z,Dic_pr,Dic_sub=Find_All_Profiles_Prob(sigma, n, k, p , beta, w)
    for i in range(20):
        print("sample", i)
        tau=generate_sample(sigma, n, k,p,  beta, w, Dic_pr, Dic_sub,Z)
        print("sample", i, ":",tau)    

    n=20
    k=10
    p=0.5
    w=[2]+([1]*(k))
    sigma=[10,16,2,3,8,5,6,9,7,12]
    beta=1
    print("sigma",sigma)
    Z,Dic_pr,Dic_sub=Find_All_Profiles_Prob(sigma, n, k, p , beta, w)
    for i in range(20):
        print("sample", i)
        tau=generate_sample(sigma, n, k,p,  beta, w, Dic_pr, Dic_sub,Z)
        print("sample", i, ":",tau)



def test_choice():
    n=10
    A=[1,3,6,7]
    tau=[4,7,9,2]
    c=Choice(A,tau,n)
    print("choice of",tau, "from", A, "is:", c)
    A=[1,3,6,7]
    tau=[4,9,2]
    c=Choice(A,tau,n)
    print("choice of",tau, "from", A, "is:", c)
    tau=[4,0,9,2]
    c=Choice(A,tau,n)
    print("choice of",tau, "from", A, "is:", c)

def test_distance():
    p=0.5
    tau=make_list_dic([1,2,3])
    sigma=make_list_dic([2,1,3])

    print("the distance between", tau, "and", sigma, "is", distance(tau,sigma,p))
    tau=make_list_dic([2,3,1])
    sigma=make_list_dic([2,1,3,4,6,5])
    print("the distance between", tau, "and", sigma, "is", distance(tau,sigma,p))
    tau=make_list_dic([2,3,6])
    sigma=make_list_dic([2,5,1])
    print("the distance between", tau, "and", sigma, "is", distance(tau,sigma,p))
    tau=make_list_dic([1,2,3,4])
    sigma=make_list_dic([4,3,2,1])
    print("the distance between", tau, "and", sigma, "is", distance(tau,sigma,p))







