import numpy as np
import mltools as ml
import matplotlib.pyplot as plt
from logisticClassify2 import *
    

iris = np.genfromtxt("data/iris.txt",delimiter=None)
X, Y = iris[:,0:2], iris[:,-1]   # get first two features & target
X,Y  = ml.shuffleData(X,Y)       # reorder randomly (important later)
X,_  = ml.transforms.rescale(X)  # works much better on rescaled data
XA, YA = X[Y<2,:], Y[Y<2]        # get class 0 vs 1
XB, YB = X[Y>0,:], Y[Y>0]        # get class 1 vs 2

print("Part 1")
ml.plotClassify2D(None, XA, YA)
plt.show()
ml.plotClassify2D(None, XB, YB)
plt.show()

learner = logisticClassify2();          # create "blank" learner
learner.classes = np.unique(YA)         # define class labels using YA or YB
wts = np.array([.5,-.25,1]); # TODO: fill in values
learner.theta = wts;                    # set the learner’s parameters
print("Part 2")
learner.plotBoundary(XA, YA)
plt.show()

print("Part 3")
print("ERROR:", learner.err(XA, YA))
print("Part 4")
ml.plotClassify2D(learner, XA, YA)
plt.show()

#learner.train(XA, YA)
print("Part 5")

learner.classes = np.unique(YB) 
learner.plotBoundary(XB, YB)
plt.show()

print("ERROR:", learner.err(XB, YB))
ml.plotClassify2D(learner, XB, YB)
plt.show()

#learner.train(XB, YB)


print("PROBLEM 2")
print("""-A-
          1. Yes, having an 'a' value of 0 and any positive 'b' value will make T[z] = 1 for any x1 > 0
          2. Yes, positive values for 'a', 'b', and 'c' will always make T[z] = 1 for any x1 > 0 && x2 > 0
          3. Yes, having any positive value for 'c' will make T[z] = 1 for any x1 and x2, because (x1 - a)^2 and (x2 - b)^2 will always be >= 0. The sum will be positive
          4. Yes, having positive values for 'a', 'b', 'c', and 'd' will make T[z] = 1 for any x1 > 0 && x2 > 0""")
print("""-B-
          1. Yes, having an 'a' value of 0 and any positive 'b' value will make T[z] = 1 for any x1 > 0
          2. Yes, positive values for 'a', 'b', and 'c' will always make T[z] = 1 for any x1 > 0 && x2 > 0
          3. Yes, having any positive value for 'c' will make T[z] = 1 for any x1 and x2, because (x1 - a)^2 and (x2 - b)^2 will always be >= 0. The sum will be positive
          4. Yes, having positive values for 'a', 'b', 'c', and 'd' will make T[z] = 1 for any x1 > 0 && x2 > 0""")
print("""-C-
          1. Yes, having an 'a' value of 0 and any positive 'b' value will make T[z] = 1 for any x1 > 0
          2. Yes, positive values for 'a', 'b', and 'c' will always make T[z] = 1 for any x1 > 0 && x2 > 0
          3. Yes, having any positive value for 'c' will make T[z] = 1 for any x1 and x2, because (x1 - a)^2 and (x2 - b)^2 will always be >= 0. The sum will be positive
          4. Yes, having positive values for 'a', 'b', 'c', and 'd' will make T[z] = 1 for any x1 > 0 && x2 > 0""")
print("""-D-
          1. Yes, having an 'a' value of 0 and any positive 'b' value will make T[z] = 1 for any x1 > 0
          2. Yes, positive values for 'a', 'b', and 'c' will always make T[z] = 1 for any x1 > 0 && x2 > 0
          3. Yes, having any positive value for 'c' will make T[z] = 1 for any x1 and x2, because (x1 - a)^2 and (x2 - b)^2 will always be >= 0. The sum will be positive
          4. Yes, having positive values for 'a', 'b', 'c', and 'd' will make T[z] = 1 for any x1 > 0 && x2 > 0""")


print("\n\n\n\n\n\nI worked by myself")