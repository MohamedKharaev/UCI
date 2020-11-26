
import numpy as np
import matplotlib.pyplot as plt

sizes = np.array([5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000])
diameters = [2, 2.2, 3, 3.1, 4.1, 4.1, 4.9, 5.1, 6, 6]

degrees1k = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 40, 41, 42, 44, 45, 46, 60, 64, 65, 67, 71, 80, 103, 106, 117, 385]
amounts1k = [296, 180, 110, 74, 65, 50, 36, 34, 20, 11, 15, 15, 8, 10, 5, 2, 8, 4, 6, 6, 3, 1, 1, 2, 6, 1, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
degrees10k = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 64, 66, 67, 69, 70, 71, 72, 74, 75, 76, 77, 80, 81, 82, 83, 84, 85, 86, 93, 94, 95, 97, 98, 100, 102, 103, 105, 106, 108, 116, 118, 119, 121, 124, 126, 131, 132, 135, 138, 142, 154, 170, 189, 200, 201, 204, 210, 218, 277, 349, 394, 400, 1180]
amounts10k = [2896, 1790, 1130, 846, 581, 485, 364, 268, 249, 175, 138, 131, 110, 75, 68, 64, 58, 44, 38, 34, 29, 33, 29, 23, 29, 18, 17, 21, 13, 11, 10, 14, 6, 10, 10, 10, 7, 7, 3, 11, 14, 4, 5, 4, 3, 2, 1, 3, 5, 6, 2, 4, 5, 3, 5, 2, 2, 1, 2, 1, 3, 4, 1, 3, 1, 2, 1, 3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 3, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]
degrees100k = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 142, 143, 144, 147, 148, 150, 151, 153, 155, 156, 157, 158, 159, 160, 162, 163, 164, 165, 166, 167, 169, 170, 171, 172, 174, 176, 177, 180, 181, 182, 183, 184, 188, 190, 193, 194, 196, 200, 201, 202, 205, 206, 208, 210, 211, 212, 219, 221, 228, 230, 232, 234, 246, 253, 257, 258, 260, 263, 264, 266, 267, 268, 269, 272, 274, 277, 281, 285, 302, 303, 305, 306, 307, 310, 319, 320, 323, 328, 342, 343, 346, 347, 352, 359, 365, 369, 371, 372, 387, 403, 415, 426, 439, 448, 458, 459, 476, 482, 483, 525, 540, 643, 818, 829, 873, 1231, 5191]
amounts100k = [28628, 18004, 11880, 8238, 6124, 4470, 3484, 2685, 2157, 1769, 1527, 1242, 1052, 877, 712, 606, 583, 545, 424, 336, 326, 303, 299, 240, 222, 217, 197, 163, 151, 156, 126, 117, 135, 97, 108, 98, 74, 78, 75, 68, 56, 57, 39, 55, 41, 58, 36, 34, 44, 26, 29, 33, 31, 29, 23, 30, 20, 23, 29, 22, 19, 13, 23, 27, 15, 19, 12, 12, 12, 16, 11, 13, 12, 10, 12, 14, 14, 11, 9, 8, 7, 9, 14, 5, 4, 7, 8, 10, 7, 1, 7, 5, 7, 7, 12, 2, 8, 10, 2, 6, 7, 5, 5, 5, 6, 3, 3, 3, 6, 5, 6, 6, 5, 4, 4, 1, 4, 3, 1, 1, 2, 4, 3, 3, 6, 4, 1, 3, 2, 4, 2, 1, 3, 5, 3, 2, 2, 1, 1, 2, 2, 2, 2, 2, 4, 2, 2, 1, 4, 2, 2, 2, 3, 1, 1, 2, 3, 3, 2, 1, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

plt.xscale('log')
plt.plot(sizes, diameters)
plt.title("Diameters of Graphs with Size N")
plt.xlabel("N")
plt.ylabel("Diameter")
plt.show()
print("""The graph shows that the Diameter of Barbasi-Albert graphs goes
up as the size (N) of the graph increases. The diameter grows proportionaly
to log(n).""")


plt.loglog(degrees1k, amounts1k)
plt.title("Degree Distribution (N = 1000)")
plt.xlabel("Degree")
plt.ylabel("Amount")
##b_fit = (sizes * .23585 - 24.12396)
#plt.loglog(sizes, b_fit, linestyle="dashed", label = 'Best Fit Line')
#plt.legend()
plt.show()
#print("Best Fit Line: ŷ = 0.23585X - 24.12396")
#print("""The graph shows a line with positive slope on the loglog graph. 
#      That would imply an equation that increases by a factor n of log(n), which
#      goes in line with what was expected of the algorithm - nlog(n)""")

plt.plot(degrees1k, amounts1k)
plt.title("Degree Distribution (N = 1000)")
plt.xlabel("Degree")
plt.ylabel("Amount")
##b_fit = (sizes * .23585 - 24.12396)
#plt.loglog(sizes, b_fit, linestyle="dashed", label = 'Best Fit Line')
#plt.legend()
plt.show()
#print("Best Fit Line: ŷ = 0.23585X - 24.12396")
#print("""The graph shows a line with positive slope on the loglog graph. 
#      That would imply an equation that increases by a factor n of log(n), which
#      goes in line with what was expected of the algorithm - nlog(n)""")

print("""The graph shows that the amount of vertices with degree x decreases, as 
x increases. There is a negative, exponential relationship between the two. The best
fit power law would be -2 """)

plt.loglog(degrees10k, amounts10k)
plt.title("Degree Distribution (N = 10000)")
plt.xlabel("Degree")
plt.ylabel("Amount")
##b_fit = (sizes * .23585 - 24.12396)
#plt.loglog(sizes, b_fit, linestyle="dashed", label = 'Best Fit Line')
#plt.legend()
plt.show()
#print("Best Fit Line: ŷ = 0.23585X - 24.12396")
#print("""The graph shows a line with positive slope on the loglog graph. 
#      That would imply an equation that increases by a factor n of log(n), which
#      goes in line with what was expected of the algorithm - nlog(n)""")

plt.plot(degrees10k, amounts10k)
plt.title("Degree Distribution (N = 10000)")
plt.xlabel("Degree")
plt.ylabel("Amount")
##b_fit = (sizes * .23585 - 24.12396)
#plt.loglog(sizes, b_fit, linestyle="dashed", label = 'Best Fit Line')
#plt.legend()
plt.show()
#print("Best Fit Line: ŷ = 0.23585X - 24.12396")
#print("""The graph shows a line with positive slope on the loglog graph. 
#      That would imply an equation that increases by a factor n of log(n), which
#      goes in line with what was expected of the algorithm - nlog(n)""")

print("""The graph shows that the amount of vertices with degree x decreases, as 
x increases. There is a negative, exponential relationship between the two. The best
fit power law would be -3 """)


plt.loglog(degrees100k, amounts100k)
plt.title("Degree Distribution (N = 100000)")
plt.xlabel("Degree")
plt.ylabel("Amount")
##b_fit = (sizes * .23585 - 24.12396)
#plt.loglog(sizes, b_fit, linestyle="dashed", label = 'Best Fit Line')
#plt.legend()
plt.show()
#print("Best Fit Line: ŷ = 0.23585X - 24.12396")
#print("""The graph shows a line with positive slope on the loglog graph. 
#      That would imply an equation that increases by a factor n of log(n), which
#      goes in line with what was expected of the algorithm - nlog(n)""")

plt.plot(degrees100k, amounts100k)
plt.title("Degree Distribution (N = 100000)")
plt.xlabel("Degree")
plt.ylabel("Amount")
##b_fit = (sizes * .23585 - 24.12396)
#plt.loglog(sizes, b_fit, linestyle="dashed", label = 'Best Fit Line')
#plt.legend()
plt.show()
#print("Best Fit Line: ŷ = 0.23585X - 24.12396")
#print("""The graph shows a line with positive slope on the loglog graph. 
#      That would imply an equation that increases by a factor n of log(n), which
#      goes in line with what was expected of the algorithm - nlog(n)""")

print("""The graph shows that the amount of vertices with degree x decreases, as 
x increases. There is a negative, exponential relationship between the two. The best
fit power law would be -4 """)