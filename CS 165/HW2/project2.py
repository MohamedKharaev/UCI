#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 01:29:50 2020

@author: mohamed
"""

import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 2500, 5000, 10000]

# hybrid_sort1
h1_Uniform_Vectors = [402, 1811, 3724, 9515, 19096, 40385]
h1_Almost_Sorted_Vectors = [363, 1811, 3786, 9153, 18160, 38617]
h1_Reverse_Vectors = [491, 1824, 3535, 9751, 18011, 37462]

# hybrid_sort2
h2_Uniform_Vectors = [289, 1628, 3214, 8979, 19586, 39244]
h2_Almost_Sorted_Vectors = [275, 1501, 3106, 8791, 18555, 38837]
h2_Reverse_Vectors = [294, 1533, 3144, 9061, 18270, 37923]

# hybrid_sort3
h3_Uniform_Vectors = [307, 1690, 3242, 9694, 20313, 43237]
h3_Almost_Sorted_Vectors = [294, 1600, 4166, 9076, 18757, 38784]
h3_Reverse_Vectors = [289, 1524, 3710, 9542, 18811, 38956]

# insertion_sort
i_Uniform_Vectors = [25, 630, 2441, 14672, 58975, 225394]
i_Almost_Sorted_Vectors = [7, 63, 169, 359, 838, 1641]
i_Reverse_Vectors = [57, 1215, 4757, 28357, 117528, 461499]

# merge_sort
m_Uniform_Vectors = [300, 1525, 3321, 8994, 18319, 38233]
m_Almost_Sorted_Vectors = [293, 1498, 3192, 8735, 17991, 37108]
m_Reverse_Vectors = [285, 1506, 3232, 8647, 18095, 37277]

# shell_sort1
s1_Uniform_Vectors = [16, 127, 281, 864, 1996, 4269]
s1_Almost_Sorted_Vectors = [12, 85, 177, 522, 1136, 2335]
s1_Reverse_Vectors = [9, 71, 157, 526, 1076, 2260]

# shell_sort2
s2_Uniform_Vectors = [15, 120, 282, 865, 1902, 4273]
s2_Almost_Sorted_Vectors = [12, 88, 188, 525, 1167, 2445]
s2_Reverse_Vectors = [10, 66, 151, 417, 917, 1978]

# shell_sort3
s3_Uniform_Vectors = [34, 261, 616, 1830, 4322, 9564]
s3_Almost_Sorted_Vectors = [30, 211, 564, 1648, 3778, 8436]
s3_Reverse_Vectors = [28, 215, 509, 1650, 3518, 8603]

# shell_sort4
s4_Uniform_Vectors = [17, 130, 290, 869, 1793, 4169]
s4_Almost_Sorted_Vectors = [13, 77, 161, 425, 913, 1839]
s4_Reverse_Vectors = [12, 63, 140, 388, 825, 1672]


plt.loglog(sizes, h1_Uniform_Vectors, label = 'Uniform Distribution')
plt.loglog(sizes, h1_Almost_Sorted_Vectors, label = "Almost Sorted Distribution")
plt.loglog(sizes, h1_Reverse_Vectors, label = "Reverse Distribtion")
plt.title("hybrid_sort1")
plt.xlabel("size of array")
plt.ylabel("microseconds to execute")
plt.legend()
plt.show()
print("Best Fit Line for Uniform Distribution: ŷ = 4.03371X - 351.80404")
print("Best Fit Line for Almost Sorted Distribution: ŷ = 3.84517X - 258.77938")
print("Best Fit Line for Reversed Distribution: ŷ = 3.72755X - 20.36611")


plt.loglog(sizes, h2_Uniform_Vectors, label = 'Uniform Distribution')
plt.loglog(sizes, h2_Almost_Sorted_Vectors, label = "Almost Sorted Distribution")
plt.loglog(sizes, h2_Reverse_Vectors, label = "Reverse Distribtion")
plt.title("hybrid_sort2")
plt.xlabel("size of array")
plt.ylabel("microseconds to execute")
plt.legend()
plt.show()
print("Best Fit Line for Uniform Distribution: ŷ = 3.97X - 481.16593")
print("Best Fit Line for Almost Sorted Distribution: ŷ = 3.91562X - 620.57176")
print("Best Fit Line for Reversed Distribution: ŷ = 3.81577X - 442.71491")


plt.loglog(sizes, h3_Uniform_Vectors, label = 'Uniform Distribution')
plt.loglog(sizes, h3_Almost_Sorted_Vectors, label = "Almost Sorted Distribution")
plt.loglog(sizes, h3_Reverse_Vectors, label = "Reverse Distribtion")
plt.title("hybrid_sort3")
plt.xlabel("size of array")
plt.ylabel("microseconds to execute")
plt.legend()
plt.show()
print("Best Fit Line for Uniform Distribution: ŷ = 4.35724X - 790.03542")
print("Best Fit Line for Almost Sorted Distribution: ŷ = 3.87619X - 226.37855")
print("Best Fit Line for Reversed Distribution: ŷ = 3.90641X - 296.7481")


plt.loglog(sizes, i_Uniform_Vectors, label = 'Uniform Distribution')
plt.loglog(sizes, i_Almost_Sorted_Vectors, label = "Almost Sorted Distribution")
plt.loglog(sizes, i_Reverse_Vectors, label = "Reverse Distribtion")
plt.title("insertion_sort")
plt.xlabel("size of array")
plt.ylabel("microseconds to execute")
plt.legend()
plt.show()
print("Best Fit Line for Uniform Distribution: ŷ = 22.68147X - 21846.52639")
print("Best Fit Line for Almost Sorted Distribution: ŷ = 0.166X - 15.6")
print("Best Fit Line for Reversed Distribution: ŷ = 46.38505X - 45423.57685")


plt.loglog(sizes, m_Uniform_Vectors, label = 'Uniform Distribution')
plt.loglog(sizes, m_Almost_Sorted_Vectors, label = "Almost Sorted Distribution")
plt.loglog(sizes, m_Reverse_Vectors, label = "Reverse Distribtion")
plt.title("merge_sort")
plt.xlabel("size of array")
plt.ylabel("microseconds to execute")
plt.legend()
plt.show()
print("Best Fit Line for Uniform Distribution: ŷ = 3.84178X - 447.6512")
print("Best Fit Line for Almost Sorted Distribution: ŷ = 3.73423X - 417.79619")
print("Best Fit Line for Reversed Distribution: ŷ = 3.75259X - 438.75928")


plt.loglog(sizes, s1_Uniform_Vectors, label = 'Uniform Distribution')
plt.loglog(sizes, s1_Almost_Sorted_Vectors, label = "Almost Sorted Distribution")
plt.loglog(sizes, s1_Reverse_Vectors, label = "Reverse Distribtion")
plt.title("shell_sort1")
plt.xlabel("size of array")
plt.ylabel("microseconds to execute")
plt.legend()
plt.show()
print("Best Fit Line for Uniform Distribution: ŷ = 0.43415X - 123.22017")
print("Best Fit Line for Almost Sorted Distribution: ŷ = 0.23669X - 42.28635")
print("Best Fit Line for Reversed Distribution: ŷ = 0.22926X - 46.64718")


plt.loglog(sizes, s2_Uniform_Vectors, label = 'Uniform Distribution')
plt.loglog(sizes, s2_Almost_Sorted_Vectors, label = "Almost Sorted Distribution")
plt.loglog(sizes, s2_Reverse_Vectors, label = "Reverse Distribtion")
plt.title("shell_sort2")
plt.xlabel("size of array")
plt.ylabel("microseconds to execute")
plt.legend()
plt.show()
print("Best Fit Line for Uniform Distribution: ŷ = 0.43242X - 133.69327")
print("Best Fit Line for Almost Sorted Distribution: ŷ = 0.24745X - 50.22573")
print("Best Fit Line for Reversed Distribution: ŷ = 0.19979X - 46.16818")


plt.loglog(sizes, s3_Uniform_Vectors, label = 'Uniform Distribution')
plt.loglog(sizes, s3_Almost_Sorted_Vectors, label = "Almost Sorted Distribution")
plt.loglog(sizes, s3_Reverse_Vectors, label = "Reverse Distribtion")
plt.title("shell_sort3")
plt.xlabel("size of array")
plt.ylabel("microseconds to execute")
plt.legend()
plt.show()
print("Best Fit Line for Uniform Distribution: ŷ = 0.97123X - 320.59691")
print("Best Fit Line for Almost Sorted Distribution: ŷ = 0.85558X - 279.11117")
print("Best Fit Line for Reversed Distribution: ŷ = 0.86646X - 337.74643")


plt.loglog(sizes, s4_Uniform_Vectors, label = 'Uniform Distribution')
plt.loglog(sizes, s4_Almost_Sorted_Vectors, label = "Almost Sorted Distribution")
plt.loglog(sizes, s4_Reverse_Vectors, label = "Reverse Distribtion")
plt.title("shell_sort4")
plt.xlabel("size of array")
plt.ylabel("microseconds to execute")
plt.legend()
plt.show()
print("Best Fit Line for Uniform Distribution: ŷ = 0.41903X - 122.56953")
print("Best Fit Line for Almost Sorted Distribution: ŷ = 0.18555X - 19.3498")
print("Best Fit Line for Reversed Distribution: ŷ = 0.16901X - 21.34589")



print("""5 points. Comparing the different Shellsort algorithms to the different Hybrid-sort algorithms,
to see which have similar running times and which ones are better than others: """)

print("""\tShell Short proved to be a faster algorithm to run. Even the slowest shell_sort3, was all-around faster
\tthan the fastest hybrid_sort2. Hybrid sort however proved to be more consistent between the different
\tdistributions. Shell sort worked best on uniform distributions.\n""")

print("""5 points. Identifying which algorithms have very different running times for the different input 
distributions and which ones have similar running times for all the different input distributions: """)

print("""\tHybrid sort and merge sort had similar running times for the 3 different distrubitions. Insertions sort
\tand shell sort had varying running times for the different distributions. Insertion sort had the fastest 
\tresuls for almost-sorted distrubtion by far, while reverse was the slowest.\n""")

print("""5 points. Identifying the algorithm you think is best. Explain whether you think this algorithm is 
the best possible sorting algorithm or if there is a different algorithm that you think might be even better: """)

print("""\tI think the best algorithm is shell sort. Between the different versions, the microseconds to execute stays 
\tpretty similar. Between the different versions, the variance in execution time for different distribtions
\tis also low. Lastly, shell_sort has some of the fastest result almong all the sorts. It does consistently
\twell across the board.""")