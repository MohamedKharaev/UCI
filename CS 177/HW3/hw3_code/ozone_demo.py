'''
UCI CS177: Gaussian Naive Bayes Ozone Level Classification
    This is DEMONSTRATION code:
    - It gives an example of how to load the ozone data,
      and compute simple statistics of this data.
    - You may (but do not have to) reuse parts of this code in your solutions.
    - It is NOT a template for the individual questions you must answer,
      for that see the main homework pdf.

VARIABLES IN 'ozone.npz'
    trainFeat: Ntrain x M matrix of real-valued environmental features
    trainLabels: Ntrain x 1 vector of class labels, 1=ozone-day, 0=not-ozone-day
    testFeat:  Ntest x M matrix of real-valued environmental features
    testLabels:  Ntest x 1 vector of class labels, 1=ozone-day, 0=not-ozone-day
    More info: http://archive.ics.uci.edu/ml/datasets/Ozone+Level+Detection
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy

# Load data
ozone = np.load('ozone.npz')
trainFeat, trainLabels = ozone['trainFeat'], ozone['trainLabels']
testFeat, testLabels = ozone['testFeat'], ozone['testLabels']
numTrain = trainFeat.shape[0]
numTest  = testFeat.shape[0]
M = trainFeat.shape[1]

# Split training data into two separate classes
trainFeat0 = trainFeat[trainLabels == 0]
trainFeat1 = trainFeat[trainLabels == 1]

# Estimate mean of Gaussian f_X|Y(x_ij | y_i)
# muhat[0,j] equals the mean of X_ij given Y_i=0
# muhat[1,j] equals the mean of X_ij given Y_i=1
muhat = np.zeros((2,M))
muhat[0] = np.mean(trainFeat0, axis=0)
muhat[1] = np.mean(trainFeat1, axis=0)

# Visualize whether mean of features differs between the two classes
plt.plot(muhat[0] - muhat[1])
plt.xlabel('Feature index')
plt.ylabel('Difference in class means')

# Naive baseline classifier:  Predict all test examples are class 0
yHat = np.zeros(numTest)

# Accuracy (fraction of test days classified correctly)
accuracy = np.sum(yHat==testLabels)/numTest
print('Test accuracy: %f' % accuracy)
falseAlarms = np.sum(np.logical_and(yHat==1, testLabels==0))
print('Test false alarms: %d' % falseAlarms)
misses = np.sum(np.logical_and(yHat==0, testLabels==1))
print('Test missed detections: %d' % misses)

# show plot
plt.show()



print("---HW3 QUESTION 2---")
print("-------PART A-------")

runtimeMean = 13
runtimeSTD = 2.0

print("1 - CDF(18) =", 1 - scipy.stats.norm.cdf(18, 13, 2))

print()
print("-------PART B-------")
print("CDF(16) - CDF(10) =", scipy.stats.norm.cdf(16, 13, 2) - scipy.stats.norm.cdf(10, 13, 2))

print()
print("-------PART C-------")
print("Z value at 1% = .233")
print(".233 = (13 - mean) / 2.0")
print("mean = 8.3473")

print()
print()
print("---HW3 QUESTION 3---")
print("-------PART A-------")
