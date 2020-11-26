#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:30:41 2020

@author: mohamed
"""

import numpy as np
import mltools as ml
import matplotlib.pyplot as plt
from scipy.linalg import svd
import mltools.transforms
    

iris = np.genfromtxt("data/iris.txt",delimiter=None)
f2_features = iris[:,0:2]

print("PROBLEM 1")
print("PART 1")
plt.scatter(f2_features[:,0:1], f2_features[:,1:2])
plt.show()
print("""I believe there are 2 clusters. One is found within 0 < x < 6
      and 3 < y < 4.5. The other is found within 4.5 < x < 8 and 2 < y < 4.""")

print("PART 2")
for k_clusters in [2, 5, 20]:
    print('K:', k_clusters)
    Zs = []
    mus = []
    ssds = []
    for i in range(5):
        Z, mu, ssd = ml.cluster.kmeans(f2_features, K = k_clusters, init = 'k++', max_iter = 100)
        Zs.append(Z)
        mus.append(mu)
        ssds.append(ssd)
    max_i = ssds.index(max(ssds))
   
    # Plotting the clustered data
    plt.scatter(f2_features[:, 0], f2_features[:, 1], c=Zs[max_i]) # Plotting the data
    plt.scatter(mu[:, 0], mus[max_i][:, 1], s=125, marker='x', facecolor='black', lw=8) # Plotting the centroids
    plt.scatter(mu[:, 0], mus[max_i][:, 1], s=7500, alpha=.45, c=np.unique(Zs[max_i])) # Lazy way of plotting the clusters area :)

    plt.show()
    
print("PART 3")
for k_clusters in [2, 5, 20]:
    print("K:", k_clusters)
    z, join = ml.cluster.agglomerative(f2_features, k_clusters, 'min')
    print('min')
    plt.scatter(f2_features[:, 0], f2_features[:, 1], c=z) # Plotting the data
    plt.show()
    z, join = ml.cluster.agglomerative(f2_features, k_clusters, 'max')
    plt.scatter(f2_features[:, 0], f2_features[:, 1], c=z) # Plotting the data
    print('max')
    plt.show()
    
print("PART 4")
print("""The results created by the k-means clustering seemed to be more equally distributed
      amongst all the points. The results both resemble similar shapes for the clusters.""")


print("PROBLEM 2")
print("PART 1")

X = np.genfromtxt("data/faces.txt", delimiter=None)  # load face dataset

f, ax = plt.subplots(2, 1, figsize=(17, 13))
ax = ax.flatten()

plt.figure()
# pick a data point i for display 
img1 = np.reshape(X[3,:],(24,24))        # convert vectorized data to 24x24 image patches
ax[0].imshow( img1.T , cmap="gray")        # display image patch; you may have to squint


mu = np.mean(X, axis = 0)
X0 = X - mu
img2 = np.reshape(X0[3,:],(24,24))        # convert vectorized data to 24x24 image patches
ax[1].imshow( img2.T , cmap="gray")        # display image patch; you may have to squint
plt.show()

print("PART 2")
U, s, V = svd(X0, full_matrices=False)
W = np.dot(U, np.diag(s))

X0 = np.dot(np.dot(U, np.diag(s)), V)
print("W shape:",W.shape)
print("V shape:",V.shape)

print("PART 3")
x_approxs = []
approx_mses = []
for k in range(12):
    x_approxs.append(np.dot(W[:, :k], V[:k, :]))
    approx_mses.append(np.mean((X0 - x_approxs[k])**2))


plt.plot(range(12), approx_mses)
plt.show()

print("PART 4")

img1s = []
img2s = []
for j in range(3):
    alpha = 2*np.median(np.abs(W[:,j]))
    img1s.append( np.reshape(mu + np.dot(alpha, V[j,:]), (24, 24)) )
    img2s.append( np.reshape(mu - np.dot(alpha, V[j,:]), (24, 24)) )
    
f, ax = plt.subplots(2, 3, figsize=(7, 4))
ax = ax.flatten()

plt.figure()
    
ax[0].imshow(img1s[0].T, cmap="gray")
ax[1].imshow(img2s[0].T, cmap="gray")
ax[2].imshow(img1s[1].T, cmap="gray")
ax[3].imshow(img2s[1].T, cmap="gray")
ax[4].imshow(img1s[2].T, cmap="gray")
ax[5].imshow(img2s[2].T, cmap="gray")

plt.show()
    
print("PART 5")

"""img3s = []
img4s = []
for K in [5, 10, 50, 100]:
    print(U.shape, np.diag(s).shape, V.shape)
    print(np.dot(np.dot(U, np.diag(s)), V).shape)
    
f, ax = plt.subplots(2, 4, figsize=(7, 4))
ax = ax.flatten()

plt.figure()
    
ax[0].imshow(img3s[0].T, cmap="gray")
ax[1].imshow(img3s[1].T, cmap="gray")
ax[2].imshow(img3s[2].T, cmap="gray")
ax[3].imshow(img3s[3].T, cmap="gray")
ax[4].imshow(img4s[0].T, cmap="gray")
ax[5].imshow(img4s[1].T, cmap="gray")
ax[6].imshow(img4s[2].T, cmap="gray")
ax[7].imshow(img4s[3].T, cmap="gray")

plt.show()
"""
print("PART 6")

idx = range(25)

coord,params = ml.transforms.rescale( W[:,0:2] )  # normalize scale of "W" locations
plt.figure();                                     # you may need this for pyplot
for i in idx:
    # compute where to place image (scaled W values) & size
    loc = (coord[i,0],coord[i,0]+0.5, coord[i,1],coord[i,1]+0.5)
    img = np.reshape( X[i,:], (24,24) )           # reshape to square
    plt.imshow( img.T , cmap="gray", extent=loc ) # draw each image
    plt.axis( (-2,2,-2,2) )                       # set axis to a reasonable scale