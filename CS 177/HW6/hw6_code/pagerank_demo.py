'''
UCI CS177: Markov chains and Pagerank
    This is DEMONSTRATION code:
    - It gives an example of how to construct a state transition matrix
      for the web link data, and use it to predict "random surfer" behavior.
    - You may (but do not have to) reuse parts of this code in your solutions.
    - It is NOT a template for the individual questions you must answer,
      for that see the main homework pdf.
'''

import numpy as np
import matplotlib.pyplot as plt

def load_data():
    # Data collected in 2002 by Prof. Jon Kleinberg, Cornell University
    # Cleaned version courtesy of ECEN5322, University of Colorado
    #  L[i,j]   = 1 if there is a directed link from website i to website j
    #  L[i,j]   = 0 if there is no directed link from website i to website j
    #  names[i] = URL of website i
    L = np.load('large_network.npz')['L']
    names = np.load('large_network.npz')['names'].tolist()
    return L, names

L, names = load_data()
m = np.shape(L)[0]  # number of websites (nodes)

# Define local random-walk state transition matrix T
T = np.array(L, np.float)
for i in range(m):
    s = np.sum(T[i])
    if s > 0:
        T[i] /= s
    else:
        T[i, i] = 1

"""PART B"""
B = np.ones((9664, 9664)) / 9664
G = (1-.15)*(T) + (.15*B)


# Find state distribution after one step of random walk from uniform init.
p0 = np.ones(m) / m
p1 = np.dot(p0, T)

"""PART C"""
pis = [];
pis.append(np.ones(m) / m)
for i in range(1, 100):
    pis.append(np.dot(pis[i - 1], G))

E = []
for i in range(1, 100):
    E.append(np.sum([(abs(pis[x] - pis[x-1])) for x in range(1, i)]))

# Display highest ranked webpages after only one step of random walk
rank_inds = np.argsort(p1)[::-1]
rank_value = p1[rank_inds]
print('pagerank\tin\tout\turl:')
for i in range(25):
    cur_ind = rank_inds[i]
    links_in  = np.sum(L[:, cur_ind])
    links_out = np.sum(L[cur_ind, :])
    print('%.5f\t\t%d\t%d\t%s' % (rank_value[i], links_in, links_out, names[rank_inds[i]]))

print("PART C")
plt.plot(range(1, 100), E)
print("limit : 1.2")
