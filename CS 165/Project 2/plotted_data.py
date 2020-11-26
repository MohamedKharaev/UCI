
import numpy as np
import matplotlib.pyplot as plt

sizes = np.array([500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000])

Next_Fit_Vectors = [116.563, 241.326, 1175.04, 2344.23, 11812, 23534.1, 117703, 235926]
First_Fit_Vectors = [168.563, 338.326, 1726.04, 3445.23, 17276, 34539.1, 172871, 346211]
First_Fit_Decreasing_Vectors = [173.563, 347.326, 1759.04, 3501.23, 17535, 35015.1, 175114, 350629]

plt.loglog(sizes, Next_Fit_Vectors, label = 'Next Fit')
plt.title("Waste for Next_Fit Algorithm")
plt.xlabel("N")
plt.ylabel("Waste(N)")
b_fit = (sizes * .23585 - 24.12396)
plt.loglog(sizes, b_fit, linestyle="dashed", label = 'Best Fit Line')
plt.legend()
plt.show()
print("Best Fit Line: ŷ = 0.23585X - 24.12396")
print("""The graph shows a line with positive slope on the loglog graph. 
      That would imply an equation that increases by a factor n of log(n), which
      goes in line with what was expected of the algorithm - nlog(n)""")

plt.loglog(sizes, First_Fit_Vectors, label = "First Fit")
plt.title("Waste for First_Fit Algorithm")
plt.xlabel("N")
plt.ylabel("Waste(N)")
b_fit = (sizes * .34616 - 37.45331)
plt.loglog(sizes, b_fit, linestyle="dashed", label = 'Best Fit Line')
plt.legend()
plt.show()
print("Best Fit Line: ŷ = 0.34616X - 37.45331")
print("""The graph shows a line with positive slope on the loglog graph. 
      That would imply an equation that increases by a factor n of log(n), which
      goes in line with what was expected of the algorithm - nlog(n)""")

plt.loglog(sizes, First_Fit_Decreasing_Vectors, label = "First Fit Decreasing")
plt.title("Waste for First_Fit_Decreasing Algorithm")
plt.xlabel("N")
plt.ylabel("Waste(N)")
b_fit = (sizes * .35057 - 19.05798)
plt.loglog(sizes, b_fit, linestyle="dashed", label = 'Best Fit Line')
plt.legend()
plt.show()
print("Best Fit Line: ŷ = 0.35057X - 19.05798")
print("""The graph shows a line with positive slope on the loglog graph. 
      That would imply an equation that increases by a factor n of log(n), which
      goes in line with what was expected of the algorithm - nlog(n)""")

print()
print()
print("""I think the best algorithm to use is Next fit, its implementable in O(N) time and
      leaves the least free space, among the ones I tested.""")
