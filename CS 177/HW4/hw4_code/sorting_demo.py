%'''
    UCI CS177: Analysis of randomized sorting algorithms.
    This is DEMONSTRATION code:
        - Shows how to create a list of random numbers and sort it
          using the provided insertion sort algorithm.
        - You may (but do not have to) reuse parts of this code in your solutions. 
        - It is NOT a template for the individual questions you must answer,
          for that see the main homework pdf.
'''

import numpy as np
from randomized_insertion_sort import randomized_insertion_sort

# Create a list of 10 random numbers in [0, 1]
unsorted_list = np.random.random(10)

# Sort the list
sorted_list, comparisons = randomized_insertion_sort(unsorted_list)

print('Unsorted list:')
print(unsorted_list)

print('\nSorted list:')
print(sorted_list)

# The number of comparisons will vary for different random number lists
print('\nNumber of comparisons:', comparisons)
