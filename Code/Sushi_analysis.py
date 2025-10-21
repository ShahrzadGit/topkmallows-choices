from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from scipy.spatial.distance import pdist, squareform
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np
import math
import time
from functools import partial
import os
import random
from collections import defaultdict
from LearningAlgos import BuCchoi
from LearningAlgos import Choice
from CreateSyntheticData import TopAssElement
from DyPChiP import DyPChIP_final
import sys




"""
File I/O 
"""


def read_preferences(file_path):
    """Read preferences from a file. Each preference list is in a separate line, prefernces are
    separated using , and they might come after :. Lines without , are skipped"""
    
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f]

    count = 0
    preferences = list()
    for l in lines:
        #print (count, ": ", l)
    
        if ',' in l: 
            num_string = l.rsplit(":", 1)[-1]
            preferences.append([int(n) for n in num_string.split(",")])
            count += 1
            
    return preferences


"""

functions needed for clustering 

"""


def position(top):
  return {t:i for i, t in enumerate(top, start = 1)}

def num_misorders(top_1, top_2, n):
  """Calculates kendal-tau distance (integral and fractional) for top-k rankings in O(k^2)"""
  count = 0
    
  if len(top_1) != len(top_2): 
    print("inconsistent k")
    return count
      
  k = len(top_1)
  pos_1 = position(top_1)
  pos_2 = position(top_2)
  s = pos_1.keys() & pos_2.keys()
  l = len(s)
  #print ("common keys: ", s)
  
  # case i \in s, j \in s, O(s^2)
  for i in s:
    for j in s: 
      if (pos_1[i] - pos_1[j]) * (pos_2[i] - pos_2[j]) < 0:
        count += 1

  # since double counting need to divide by 2.
  count /= 2

  #print("total distance for s x s: ", total_distance)
   
  # case i \in top_1\s, j \in s, O(k * s)
  for i in top_1:
    for j in s:
      if i in s: 
        continue
      if pos_1[i] < pos_1[j]:
        count += 1 
  #print("total distance updated after adding top_1\\s x s: ", total_distance)

  # case i \in top_2\s, j \in s, O(k * s)
  for i in top_2:
    for j in s:
      if i in s:
        continue
      if pos_2[i] < pos_2[j]:
        count += 1

  # case i \in top_2\s, j \in top_1\s or vice-versa, O(1)
  count += (k-l) * (k-l)
  #print("total distance updated after adding top_2\\s x top_1\\s or vice-versa: ", total_distance)

  return count

def num_incomparable_diff(top_1, top_2, n):
  """computes poition and then after thay it is just O(1)."""
  count = 0
    
  if len(top_1) != len(top_2): 
    print("inconsistent k")
    return count
      
  k = len(top_1)
  pos_1 = position(top_1)
  pos_2 = position(top_2)
  s = pos_1.keys() & pos_2.keys()
  l = len(s)
    
  count = 0
  #print("total distance updated after adding top_2\\s x s: ", total_distance)

  # case i \in top_1\s, j \in top_1\s and i \in top_2\s , j \in top_2\s, O(1) 
  count += (k-l) * (k-l-1) 
  #print("total distance updated after adding top_1\\s x top_1\\s and top_2\\s x top_2\\s: ", total_distance)

  # case i \in bag\(top_1 U top_2), j \in top_1\s or j \in top_2\s, O(1)
  count += (k-l) * (n-2*k+l) * 2
  #print("total distance updated after adding bag\\(top_1 U top_2) x [top_1\\s or top_2\\s]: ", total_distance)

  return count

def disagreements (rankings, num_elements):
    num_rankings = len(rankings)
    misorders = np.zeros((num_rankings,num_rankings))
    incomparables = np.zeros((num_rankings,num_rankings))
    for i in range(num_rankings):
        if i % 100 == 0: print(i)
        for j in range(i + 1, num_rankings):
            #print("ranking a ", rankings[i])
            #print("ranking b ", rankings[j])
            misorders[i][j] = misorders[j][i] = num_misorders(rankings[i], rankings[j], num_elements)
            #print("num_misorders between {} and {} is {} ".format(rankings[i], rankings[j], misorders_ij))
            incomparables[i][j] = incomparables[j][i] = num_incomparable_diff(rankings[i], rankings[j], num_elements)
            #print("num_incomparables between {} and {} is {} ".format(rankings[i], rankings[j], incomparables_ij))
       
    return misorders, incomparables

def dist_kendal_tau(top_1, top_2, n, p, beta):
    misorders = num_misorders(top_1, top_2, n)
    incomparables = num_incomparable_diff(top_1, top_2, n)
    return misorders +( p * incomparables)
    #return math.exp(-beta * (misorders + incomparables * p)) 


def cluster_preferences(preferences, misorders, incomparables, n , p ):

    snapshot_time = time.time()
    #param_kendal_tau = partial(exp_kendal_tau, n, p, beta)
    #dist_array = pdist(preferences, metric=param_kendal_tau)  # 1D condensed form
    #dist_matrix = squareform(dist_array)       # Convert to square matrix
    #dist_matrix = misorders + 0.001 * incomparables
    dist_matrix = misorders + (p * incomparables)
    # print("dist_matrix constructed in ", time.time() - snapshot_time)
    # print("dist_matrix[:10, :10]: ", dist_matrix[:10,:10])
    # print("misorders[:10, :10]: ", misorders[:10,:10])
    # print("incomparables[:10, :10]: ", incomparables[:10,:10])
    snapshot_time = time.time()


    # Perform hierarchical clustering
    Z = linkage(dist_matrix, method='average')  # or 'complete', 'single'
    print("linkage completed in ", time.time() - snapshot_time)

    return Z



def find_emperical_probs(S,A):
   n=100
  # print("finding emperical estimations from test set")
   counts={key:0 for key in A+[0]}
   m=len(S)
   for tau in S:
     
      y=Choice(A, tau,n)
    #  print("tau", tau, "choice", y)
      counts[y]=counts[y]+1
   emperical_probs= {k: (v/m) for k, v in counts.items()}
   return emperical_probs

def Learn_choiceprobs_MM(A,beta_range,n,p,size_of_data,clusters):
   print("#  Learning probs for MM model, A =",A) 
   list_of_dicprobs_forall_betas=[]
   
  
   list_of_centers=[]
   list_of_weights=[]
   for label in clusters:
         cluster_weight = len(clusters[label]) / size_of_data
         print("#cluster ",label, "with weight",  cluster_weight ) 
         learned_cluster_center_dic, learned_cluster_center_list= BuCchoi(range(1,n+1),clusters[label])
         print("Learned cluster center of cluster {}: ".format(label), learned_cluster_center_dic, learned_cluster_center_list)
      # Calculate choice probability of each item using DYCHIP

      
         k=len(learned_cluster_center_list)
         if k>12:
            learned_cluster_center_list=learned_cluster_center_list[:12]
         list_of_centers=list_of_centers+[learned_cluster_center_list]   
         list_of_weights=list_of_weights+[cluster_weight]
   list_of_dicprobs_forall_betas=[]
   
   for i in range(len(beta_range)):
         learned_prob_dic={key:0 for key in ANull}
         beta=beta_range[i]
         for clus_num in range(len(list_of_centers)):
            cluster_center=list_of_centers[clus_num]
            cluster_weight=list_of_weights[clus_num]

            k=len(cluster_center)   
            w=[1 for i in range(k+1)]
      
      
            item_probability_for_cluster=DyPChIP_final(A,  cluster_center, n, k, p , beta, w)
       
         #print("learned probs for cluster", label, "\n")
         #print(item_probability_for_cluster)
         #item_probability_for_cluster = np.ones(n)/n #DYCHIP(learned_cluster_center, clusters[label])
        
            for it in ANull:
                learned_prob_dic[it]=learned_prob_dic[it]+(item_probability_for_cluster[it]* cluster_weight)
         
         #print("cluster label", label, "learned center: \n " ) 
         #print("sigma=",learned_cluster_center_list)
           # print("learned probs (dictionary) for beta:",beta,"\n")
            #print("probs=",learned_prob_dic)
      #print("choice probs for this beta:", learned_prob_dic)   
         list_of_dicprobs_forall_betas=list_of_dicprobs_forall_betas+[learned_prob_dic] 
   return list_of_dicprobs_forall_betas 
def Learn_utilities_MNL(train):
    # we set the utility of item 0 to a fixed value and calculate all other utilities with respect to it
    fixed_val=1
    u = np.zeros(n+1)
    u[0] = fixed_val
    for i in range(1, n+ 1):
        A = [i]
        count = np.sum([1 for tau in train if Choice(A,tau,n) != 0])
        u[i] = count / (fixed_val * len(preferences))

    u_total = np.sum(u)
    u_normalized = u / u_total 
    return u_normalized

def choice_probs_MNL(utilities,A):
   ANull=A+[0]
   u_A=[utilities[i] for i in ANull]
   total_u=sum(u_A)
   probs={k:(utilities[k]/total_u) for k in ANull }
   return probs

def learn_sushi_center(n,p,beta,data,num_runs):
   Nnull=list(range(n+1))
   
   item_scores_partial={key:0 for key in Nnull}
  
   for i in range(num_runs):
       learned_cluster_center_dic, learned_cluster_center_list=BuCchoi(range(1,n+1),data)
       for key in Nnull:
          item_scores_partial[key]=item_scores_partial[key]+learned_cluster_center_dic[key]
    
   aggregate_center_for_all_runs=sorted( Nnull, key=lambda x: item_scores_partial[x])
   return aggregate_center_for_all_runs
   
          
          
      
   
   
      
   
"""

Processing Sushi Data-set 

"""

# file directories 

file_dir =  # Sushi data set address 
file_name =  # cleaned file 
file_type =  #, ".soc"]#, ".toi"]
myresults= # where to store the analysis results 

n = 100 
file_path = file_dir + file_name + file_type

start = time.time()
print("reading prefrences", flush=True)
preferences = read_preferences(file_path)
#count number of misorders (I_i) and incomparables (P_i) separately and save to a file for future usecases. 
misorders, incomparables = disagreements(preferences, n)
np.save(file_path + "_misorders.npy", misorders)
np.save(file_path + "_incomparables.npy", incomparables)
# read number of misorders and incomparables from file
dist_misorders = np.load(file_path + "_misorders.npy")
dist_incomparables = np.load(file_path + "_incomparables.npy")


item_set = np.arange(1,n+1)
num_preferences = len(preferences)

random.seed(42)
all_indices = list(range(num_preferences))


"""
comparision with MNL and hyperparameter tunning

"""

# split training set and test set in each cluster 


item_set = np.arange(1,n+1)
num_preferences = len(preferences)
train_size = int( num_preferences * .8)
random.seed(42)
all_indices = list(range(num_preferences))
train_indices = random.sample(all_indices, train_size)
test_indices = list(set(all_indices) - set(train_indices))
train = [preferences[i] for i in train_indices]
test = [preferences[i] for i in test_indices]



#  p_range=[0.01, 0.025,  0.05, 0.075, 0.1, 0.25, 0.5,1, 1.5,  2, 2.5,5]
p=  0.5
num_clusts=1
num_runs=10
r=6

outputfile_name= myresults
sys.stdout = open(outputfile_name, 'w')




# find MNL utilities 

print("p=",p, "num clusters=", num_clusts)

if (num_clusts!=1): 
    Z = cluster_preferences(train, dist_misorders[train_indices], dist_incomparables[train_indices], n = 100, p = p)
    labels = fcluster(Z, t=num_clusts, criterion='maxclust')
    sil_score = silhouette_score(train, labels)
    print("silhouette_score of the clusters",  sil_score )
    clusters = defaultdict(list)
    for point, label in zip(train, labels):
      clusters[label].append(point)
else: 
    labels = np.ones(len(train), dtype=int)  # Safer than using train_size if not defined
    clusters = {1: list(train)}

       


list_of_utilities=[]
cluster_weight_list=[]

for label in clusters:
   learned_utilities= Learn_utilities_MNL(clusters[label]) 
   cluster_weight = len(clusters[label]) / train_size
   list_of_utilities=list_of_utilities+[learned_utilities]
   cluster_weight_list=cluster_weight_list+[cluster_weight]

 
  
beta_range=[0.025,0.05,0.1,0.25,0.5,0.75,1,1.25,1.5,1.75,2]

errlist_across_allassorts_indexed_by_beta=[[] for i in beta_range]
errlist_across_allassorts_forMNL=[]
for i in range(num_runs):
     mean_gen_error_for_allbetas=[]
     r1=math.floor(r/2)
     A=random.sample(range(1,10), r1)+random.sample(range(10,n+1), r-r1)
     ANull=A+[0]
     print("sampled assortment", A, "number:",i)
     learned_prob_dic=Learn_choiceprobs_MM(A,beta_range,n,p,train_size,clusters)
     list_of_dicprobs_forall_betas=Learn_choiceprobs_MM(A,beta_range,n,p,train_size,clusters)
     test_probs=find_emperical_probs(test,A)
     print("empirical probabilities from test set:", test_probs)
     err_list_forall_betas_thisassort=[]
     for i in range(len(beta_range)):
       learned_prob= list_of_dicprobs_forall_betas[i]
       err_dic={k:0 for k in ANull}
       print("results for assortment",A, ":\n")
       for it in ANull:      
          err_dic[it]=abs(learned_prob[it]-test_probs[it])
       print("beta is ",beta_range[i],"\n")
       print("learned probs for this beta:",learned_prob ) 
       print("err dic=",err_dic, "\n")
       print("err list=",list(err_dic.values()))
       err_list_forall_betas_thisassort= err_list_forall_betas_thisassort+[np.mean(list(err_dic.values()))]
       errlist_across_allassorts_indexed_by_beta[i]= err_list_forall_betas_thisassort
      #we now find the error for MNL
    
     for it in ANull:
        learned_probs_MNL={k:0 for k in ANull}
        for cl in range(len(list_of_utilities)):
            learned_probs_MNL_thiscluster=choice_probs_MNL(list_of_utilities[cl],A)
            w=cluster_weight_list[cl]
            learned_probs_MNL[it]=learned_probs_MNL[it]+learned_probs_MNL_thiscluster[it]*w


     err_dic={k:0 for k in ANull}
     print("results for assortment",A, ":\n")
     for it in ANull:  
          err_dic[it]=abs(learned_probs_MNL[it]-test_probs[it])
     print("err MNL dic=",err_dic, "\n")
     print("err MNL list=",list(err_dic.values()))
     errlist_across_allassorts_forMNL=errlist_across_allassorts_forMNL+[np.mean(list(err_dic.values()))]    

mean_err=np.zeros(len(beta_range))   
std_err=np.zeros(len(beta_range))       
for i in range(len(beta_range)):
     this_beta=np.array(errlist_across_allassorts_indexed_by_beta[i])
     mean_err[i]=np.mean(this_beta)
     std_err[i]=np.std(this_beta)
     
print("****final outcomes:*****")   
print("beta range:",beta_range)  
print(" mean error for all betas:\n")
print("mean_err=",mean_err)
print("mean_std=", std_err)
err_MNL_arr=np.array(errlist_across_allassorts_forMNL)
print("MNL:",err_MNL_arr)
mean_err_MNL=np.mean(err_MNL_arr)
var_err_MNL=np.std(err_MNL_arr)
print(" mean error for MNL:\n")
print("mean_err_MNL=",mean_err_MNL)
print("mean_std_MNL=", var_err_MNL)







