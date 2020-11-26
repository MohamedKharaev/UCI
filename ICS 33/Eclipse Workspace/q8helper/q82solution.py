# Put imports here
import cProfile
import nearestneighbor
import random
import pstats

# Put code for profile analysis here 

coords = []
for i in range(25600):
    coords.append((random.random(), random.random()),)
    
cProfile.run('nearestneighbor.closest_2d(coords)', 'q82output.txt')

stats = pstats.Stats('q82output.txt')
stats.sort_stats('ncalls')

stats.print_stats(15)

stats.sort_stats('tottime')

stats.print_stats(15)