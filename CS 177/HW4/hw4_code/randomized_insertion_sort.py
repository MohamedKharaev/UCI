import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns

def randomized_insertion_sort(L):
    '''
    Sort an array and count comparisons using randomized insertion sort
    Inputs:
    L:      Vector to sort

    Outputs:
    L:      Sorted vector
    comps:  Number of comparisons made in insertion sort
    '''
    
    L = np.random.permutation(L)
    comps = 0
    for ind in range(1, len(L)):
        for x in range(ind, 0, -1):
            comps += 1
            if L[x] < L[x-1]: 
                L[[x, x-1]] = L[[x-1, x]]
            else:
                break
    return L, comps
            
            

print("-----PART A-----")
print()
print("(n^2 - n)")
print("---------")
print("    2    ")
print()
print("-----PART B-----")
print()
print("-----PART C-----")
print()
rand = []
for i in range(1000):
    rand.append(randomized_insertion_sort(10)[1])
average = sum(rand) / 1000
print("Average of 1000 trials:", average)
x = np.sort(rand)
n = x.size
y = np.arange(1, n + 1) / n

plt.scatter(x = x, y = y)
plt.show()
print("-----PART D-----")
print()
rand = []
for i in range(1000):
    rand.append(randomized_insertion_sort(100)[1])
average = sum(rand) / 1000
print("Average of 1000 trials:", average)
x = np.sort(rand)
n = x.size
y = np.arange(1, n + 1) / n

plt.scatter(x = x, y = y)
plt.show()

print("the distribution of comparisons does not change as the list length grows. Only the amount of comparisons changse")