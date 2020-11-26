import numpy as np
import matplotlib.pyplot as plt
import mltools as ml

data = np.genfromtxt("data/curve80.txt", delimiter=None)
X = data[:,0]
X = np.atleast_2d(X).T
Y = data[:,1]
Xtr, Xte, Ytr, Yte = ml.splitData(X,Y,0.75)

print("---PROBLEM 1---")
print("\n-Part 1-")
print("Xtr Shape:", Xtr.shape)
print("Xte Shape:", Xte.shape)
print("Ytr Shape:", Ytr.shape)
print("Yte Shape:", Yte.shape)

print("\n-Part 2-")
lr = ml.linear.linearRegress(Xtr, Ytr)
xs = np.linspace(0, 10, 200)
xs = xs[:,np.newaxis]
ys = lr.predict(xs)

# Plotting the data
f, ax = plt.subplots(1, 1, figsize=(10, 8))
    
ax.scatter(Xtr, Ytr, s=80, color='blue', alpha=0.75, label='Train')
ax.scatter(Xte, Yte, s=240, marker='*', color='red', alpha=0.75, label='Test')

# Also plotting the regression line
ax.plot(xs, ys, lw=3, color='black', alpha=0.75, label='Prediction')

ax.set_xticklabels(ax.get_xticks(), fontsize=25)
ax.set_yticklabels(ax.get_yticks(), fontsize=25)   

# Controlling the size of the legend and the location.
ax.legend(fontsize=30, loc=4)

plt.show()    

print("Linear coefficients:", lr.theta)

def MSE(y_true, y_hat):
    l = len(y_true)
    assert l == len(y_hat)
    sum = 0;
    for i in range(l):
        sum += ((y_hat[i] - y_true[i]) ** 2)
    return sum / l

print("MSE Training:", MSE(Xtr, Ytr))
print("MSE Testing :", MSE(Xte, Yte))

print("\n-Part 3-")

def Phi(X):
  return ml.transforms.rescale( ml.transforms.fpoly(X, degree,False), params)[0]

Xtr2 = np.zeros( (Xtr.shape[0], 2) )
Xtr2[:,0] = Xtr[:,0]
Xtr2[:,1] = Xtr[:,0]**2

xs = np.linspace(0, 10, 200)
xs = np.atleast_2d(xs).T
d = np.array([1, 3, 5, 7, 10, 18])
yss = []

for degree in d:
    XtrP = ml.transforms.fpoly(Xtr, degree, bias=False)
    XtrP,params = ml.transforms.rescale(XtrP)
    xsP = ml.transforms.fpoly(xs, degree, bias=False)
    xsP,params = ml.transforms.rescale(xs)
    lr = ml.linear.linearRegress( XtrP, Ytr )
    yss.append(lr.predict(Phi(xsP)))
    
fig, ax = plt.subplots(1, 1, figsize=(10, 8))
ax.plot(xs, yss[0], color='black') # Plot for each polynomial degree
ax.plot(xs, yss[1], color='blue') # like so
ax.plot(xs, yss[2], color='yellow')
ax.plot(xs, yss[3], color='red')
ax.plot(xs, yss[4], color='green')
ax.plot(xs, yss[5], color='purple')
ax.set_ylim(-5, 5) # Set the minimum and maximum limits
plt.show()
    
mse_error = np.zeros(d.shape[0])

for i, degree in enumerate(d):
    XtrP = ml.transforms.fpoly(Xtr, degree, False)

    lr = ml.linear.linearRegress(XtrP, Ytr)
    XteP = ml.transforms.fpoly(Xte, degree, False)
    YteHat = lr.predict(XteP)

    mse_error[i] = MSE(Yte, YteHat)
    
f, ax = plt.subplots(1, 1, figsize=(10, 8))

# Plotting a line with markers where there's an actual x value.
ax.semilogy(d, mse_error, lw=4, marker='d', markersize=20, alpha=0.75, label='MSE ERROR')


# Setting the X-ticks manually.
ax.set_xticks(np.arange(2, 21, 2))

ax.set_xticklabels(ax.get_xticks(), fontsize=25)
ax.set_yticklabels(ax.get_yticks(), fontsize=25)   

ax.legend(fontsize=20, loc=0)

plt.show()

print("I recommend degree 7")

print("---PROBLEM 2---")
print("\n-Part 1-")

def DegreeCrossValidation(nFolds, degree, Xtr, Ytr):
    J = dict()
    XtrP = ml.transforms.fpoly(Xtr, degree, bias=False)
    XtrP,params = ml.transforms.rescale(XtrP)
    for iFold in range(nFolds):
        Xti,Xvi,Yti,Yvi = ml.crossValidate(XtrP,Ytr,nFolds,iFold)
        learner = ml.linear.linearRegress(Xti, Yti)
        J[iFold] = MSE(Yvi, learner.predict(Xvi))
    return (sum([x[0] for x in J.values()]) / 5)


y = []
for degree in d:
    y.append(DegreeCrossValidation(5, degree, Xtr, Ytr))
plt.semilogy(d, y)
plt.show()


print("\n-Part 2-")
print("""The 5-fold data shows a similar trend to the MSE values of the true data.
      The main differences are the trend found between the lower degrees, and 
      the MSE values at higher degrees. The MSE values of the 5-fold data are much higher
      at degree 10 and and 18. There is also a raise in error between degree 3 and 5
      in the 5-fold data, while the true data evaluates the MSE as the same.""")

print("\n-Part 3-")
print("I recommend degree 7")

print("\n-Part 4-")

y2 = []
nFold = [2, 3, 4, 5, 6, 10, 12, 15]
for nFolds in nFold:
    y2.append(DegreeCrossValidation(nFolds, 7, Xtr, Ytr))
plt.semilogy(nFold, y2)
plt.show()
print("""As the k increases, the error increases as well. Normally this is not the case,
      but I think that it is occuring here because of the degree of the graph. The
      approximations made by the graph with degree 7 are very accurate between values 4
      and 9. Because of that, increasing the amount of folds, therefore checking error
      on more sections that are outside of those bounds, creates a higher average error.""")
