import math
import sys

class StoogeSort:
	def __init__(self):
		self.ops = 0
		
	def resetOps(self):
		self.ops = 0

	def sort(self,A,i,j):
		n = j - i + 1
		if n == 2:
			#swap A[i] and A[j]
			self.ops += 1
			if A[i] > A[j]:	
				A[i] += A[j]
				A[j] = A[i] - A[j]
				A[i] = A[i] - A[j]
			#for thing in A:
			#	sys.stdout.write(str(thing) + ' ')
			#sys.stdout.write('\n')
		elif n > 2:
			#for thing in A:
			#	sys.stdout.write(str(thing) + ' ')
			#sys.stdout.write('\n')
			m = math.floor(n/3)
			A = self.sort(A, i, j - m) #sort first 2/3rds
			A = self.sort(A, i + m, j) #sort second 2/3rds
			A = self.sort(A, i, j - m) #sort first 2/3rds
		return A