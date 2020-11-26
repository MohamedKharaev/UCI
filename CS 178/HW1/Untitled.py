import numpy as np
import matplotlib.pyplot as plt
import mltools as ml

iris = np.genfromtxt("data/iris.txt", delimiter=None)
Y = iris[:,-1]
X = iris[:,0:-1]

print("---PROBLEM 1---")
print("\n-Part 1-")
print("Features:", X.shape[1])
print("Data Points:", X.shape[0])

print("\n-Part 2-")
# 0 : 0 - 48
# 1 : 49 - 97
# 2 : 97 - 
fig, axs = plt.subplots(3, 4)
axs[0,0].hist(X[:48, 0], 3)
axs[0,1].hist(X[:48, 1], 3)
axs[0,2].hist(X[:48, 2], 3)
axs[0,3].hist(X[:48, 3], 3)
axs[1,0].hist(X[49:97, 0], 3)
axs[1,1].hist(X[49:97, 1], 3)
axs[1,2].hist(X[49:97, 2], 3)
axs[1,3].hist(X[49:97, 3], 3)
axs[2,0].hist(X[99:, 0], 3)
axs[2,1].hist(X[99:, 1], 3)
axs[2,2].hist(X[99:, 2], 3)
axs[2,3].hist(X[99:, 3], 3)
plt.show()
##plt.hist(Y)

print("\n-Part 3-")
print("\nFeature 1")
print("Mean:", np.mean(X[:, 0]))
print("Variance:", np.var(X[:, 0]))
print("Standard Deviation:", np.std(X[:, 0]))
print("\nFeature 2")
print("Mean:", np.mean(X[:, 1]))
print("Variance:", np.var(X[:, 1]))
print("Standard Deviation:", np.std(X[:, 1]))
print("\nFeature 3")
print("Mean:", np.mean(X[:, 2]))
print("Variance:", np.var(X[:, 2]))
print("Standard Deviation:", np.std(X[:, 2]))
print("\nFeature 4")
print("Mean:", np.mean(X[:, 3]))
print("Variance:", np.var(X[:, 3]))
print("Standard Deviation:", np.std(X[:, 3]))

print("\n-Part 4-")
plt.scatter(X[:, 0], X[:, 1], s=130, c=X[:, -1]//1, alpha=0.75)
plt.show()
plt.scatter(X[:, 1], X[:, 2], s=130, c=X[:, -1]//1, alpha=0.75)
plt.show()
plt.scatter(X[:, 2], X[:, 3], s=130, c=X[:, -1]//1, alpha=0.75)
plt.show()


print("---PROBLEM 2---")
print("\n-Part 1-")
print("A matrix is invertible iff its determinant is non-zero")

print("\n-Part 2-")
A = np.array([[1, 2, 2],
              [2, -1, 1],
              [1, 3, 2]])
B = np.array([[0, -3, -2],
              [1, -4, -2],
              [-3, 4, 1]])
print("A determinent:", np.linalg.det(A))
print("B determinent:", np.linalg.det(B))

print("\n-Part 3-")
print("A inverse:\n", np.linalg.inv(A))
print("B inverse:\n", np.linalg.inv(B))

print("\n-Part 4-")
print("Transposed A inverse:\n", np.linalg.inv(A.transpose()))
print("Transposed B inverse:\n", np.linalg.inv(B.transpose()))

print("\n-Part 5-")
C = np.matmul(A, B)
print("C inverse:\n", np.linalg.inv(C))


print("---PROBLEM 3---")
print("\n-Part 1-")
iris = np.genfromtxt("data/iris.txt",delimiter=None)  # load the data
Y = iris[:,-1]
X = iris[:,0:2]

X,Y = ml.shuffleData(X,Y);
Xtr,Xva,Ytr,Yva = ml.splitData(X,Y, 0.8);

for k in [1, 5, 10, 50]:
    knn = ml.knn.knnClassify( Xtr, Ytr, k );
    YvaHat = knn.predict( Xva );
    print("k =",k)
    ml.plotClassify2D( knn, Xtr, Ytr );
    
print("""Increasing the k values creates greater distinctions between the zones in the graph used to categorize outcomes.
      Having a k-value that is too high will however remove any islands from the graph. This could result in 
      wrong predictions for some cases. Having the K too low does not do well because the AI doesn't learn much,
      the AI instead will just repeat the information it was given when trying to predict new info.""")

print("\n-Part 2-")
def similar_accuracy(list1, list2):
    l = len(list1)
    if l != len(list2):
        return 0
    similar = 0
    for i in range(l):
        if list1[i] == list2[i]:
            similar += 1
    return similar / l

K=[1,2,5,10,50,100,200];
errTrain = [None] * len(K)
for i,k in enumerate(K):
    learner = ml.knn.knnClassify( Xtr, Ytr, k ); # TODO: complete code to train model
    Yhat = learner.predict( Xva ) # TODO: predict results on training data
    errTrain[i] = similar_accuracy(Yhat, Yva)     # TODO: count what fraction of predictions are wrong
    #TODO: repeat prediction / error evaluation for validation data
plt.semilogx(K, errTrain, 'r-', lw=3, label='Error')  #TODO: average and plot results on semi-log scale
print(errTrain)
print("I recommend a k-value of 10") 

print("\n-Part 3-")
iris = np.genfromtxt("data/iris.txt",delimiter=None)  # load the data
Y = iris[:,-1]
X = iris[:,0:-1]

X,Y = ml.shuffleData(X,Y);
Xtr,Xva,Ytr,Yva = ml.splitData(X,Y, 0.8);

K=[1,2,5,10,50,100,200];
errTrain = [None] * len(K)
for i,k in enumerate(K):
    learner = ml.knn.knnClassify( Xtr, Ytr, k ); # TODO: complete code to train model
    Yhat = learner.predict( Xva ) # TODO: predict results on training data
    errTrain[i] = similar_accuracy(Yhat, Yva)     # TODO: count what fraction of predictions are wrong
    #TODO: repeat prediction / error evaluation for validation data
plt.semilogx(K, errTrain)  #TODO: average and plot results on semi-log scale
print(errTrain)
print("The plots are not very different. The graph with more features has lower error, however that can be attributed to more information being present. I wouldn't change my k-value reccomendation.")