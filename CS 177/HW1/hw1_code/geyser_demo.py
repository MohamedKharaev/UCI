'''
 UCI CS 177: Old Faithful Geyser Data Statistics
 This is DEMONSTRATION code:
 - It gives an example of how to load the geyser data, plot the data,
   and compute simple statistics of this data.
 - You may (but do not have to) reuse parts of this code in your solutions. 
 - It is NOT a template for the individual questions you must answer,
   for that see the main homework pdf.

 Description of data:
   Waiting time between eruptions and the duration of the eruption
   for the Old Faithful geyser in Yellowstone National Park, Wyoming, USA.

 eruptions (numeric)  Eruption time in minutes
 waiting   (numeric)  Waiting time to next eruption in minutes
 
 References:
 - Hardle, W. (1991) Smoothing Techniques with Implementation in S.
   New York: Springer.
 - Azzalini, A. and Bowman, A. W. (1990). A look at some data on the
   Old Faithful geyser. Applied Statistics 39, 357-365.
'''
 
import numpy as np
import matplotlib.pyplot as plt

# Load data 
S = np.load('eruptions.npy')  # vector of observed eruption times
T = np.load('waiting.npy')    # vector of observed waiting times
n = S.shape[0]                # number of observations

# Plot data
plt.plot(S, T, 'ok')
plt.xlabel('Eruption Time (minutes)')
plt.ylabel('Waiting Time to Next Eruption (minutes)')
plt.show()

# Compute mean under empirical distribution
meanS = np.sum(S)/n
meanT = np.sum(T)/n

# Thresholds used to define X,Y variables in parts (c,d)
threshX = 3.5
threshY = 70

# Part A
Ssquared = S
Ssquared = Ssquared**2

eOfSSquared = np.sum(Ssquared) / 272
eOfSAllSquared = (np.sum(S) / 272)**2

varS = eOfSSquared - eOfSAllSquared

Tsquared = T
Tsquared = Tsquared**2

eOfTSquared = np.sum(Tsquared) / 272
eOfTAllSquared = (np.sum(T) / 272)**2

varT = eOfTSquared - eOfTAllSquared

print("---PART A---")
print("Variance of S:", varS)
print("Variance of T:", varT)
print()

# Part B

sortedS = np.argsort(S)
Squartile = int(sortedS[67])
Shalfway = int(sortedS[135])
S3quartile = int(sortedS[203])

sortedT = np.argsort(T)
Tquartile = int(sortedT[67])
Thalfway = int(sortedT[135])
T3quartile = int(sortedT[203])

print("---PART B---")
print("S1:", S[Squartile])
print("S2:", S[Shalfway])
print("S3:", S[S3quartile])
print("T1:", T[Tquartile])
print("T2:", T[Thalfway])
print("T3:", T[T3quartile])
print()

# Part C

print("---PART C---")
print("Pxy(0, 0) =", np.sum((S <= 3.5)/n) * np.sum((T <= 70)/n))
print("Pxy(1, 0) =", np.sum((S > 3.5)/n) * np.sum((T <= 70)/n))
print("Pxy(0, 1) =", np.sum((S <= 3.5)/n) * np.sum((T > 70)/n))
print("Pxy(1, 1) =", np.sum((S > 3.5)/n) * np.sum((T > 70)/n))

print("Px(0) =", np.sum((S <= 3.5)/n))
print("Px(1) =", np.sum((S > 3.5)/n))
print("Py(0) =", np.sum((T <= 70)/n))
print("Py(1) =", np.sum((T > 70)/n))
print()

# Part D

print("---PART D---")
print("""I think the variables X and Y are not independent. Based on the probability mass
functions for X and Y, it seems as though X = 0 and Y = 0 have the same probability,
as well as X = 1 and Y = 1 having the same probability. This proves that the random
observations depict a relationship between X and Y.""")
