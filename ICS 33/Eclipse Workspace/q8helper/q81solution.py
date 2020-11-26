# Put imports here
import nearestneighbor
import performance
import random
# Put code for performance analysis here 

def setup(size):
    global rand_lst
    rand_lst = []
    for i in range(size):
        rand_lst.append((random.random(), random.random()),)

def code():
    global rand_lst
    nearestneighbor.closest_2d(rand_lst)

for i in range(0, 9):
    size = 100 * (2 ** i)
    p = performance.Performance(lambda : code(), lambda: setup(size), 5, '\n\nNearest Neighbor, size = ' + str(size))
    p.evaluate()
    p.analyze()
    
