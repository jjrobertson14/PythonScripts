import random
import math
import sys

import HW7 as h
# h1 = h.HW7(2,0,1)
# B = []
# for i in range(1,5):
	# B.append(0)
	# B.append(1)
	# B.append(2)
# random.shuffle(B)
# for thing in B:
	# sys.stdout.write(str(thing) + ' ')
# sys.stdout.write('\n')
# h1.colorSort(B,0,len(B)-1)
# for thing in B:
	# sys.stdout.write(str(thing) + ' ')
# sys.stdout.write('\n')
# print ('hi')

h1 = h.HW7(1,2,3)
N = [ i for i in range(1,21)]
random.shuffle(N)
B = N[:]
random.shuffle(B)
for thing in N:
	sys.stdout.write(str(thing) + ' ')
sys.stdout.write('\n')
for thing in B:
	sys.stdout.write(str(thing) + ' ')
sys.stdout.write('\n')