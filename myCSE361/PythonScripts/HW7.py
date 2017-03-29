import math
import random

class HW7:

	def __init__(self):
		self.ops = 0
	
	def __init__(self,red,blue,green):
		self.ops = 0
		self.red,self.blue,self.green = red,blue,green
		
	def resetOps(self):
		self.ops = 0
		
	def colorSort(self,A,a,b):
		if a >= b:
			return
		p = self.colorPartition(A,a,b)
		self.colorSort(A,a,p-1)
		self.colorSort(A,p+1,b)
		
	def colorPartition(self,A,a,b):
		l = a
		r = b - 1
		p = A[b]
		
		while l <= r:
			while A[l] <= p and l <= r:
				l += 1
			while A[r] >= p and r >= l:
				r -= 1
			if l < r:
				A[l],A[r] = A[r],A[l]
		A[l],A[b] = A[b],A[l]
		return l
		
	def nutBoltSort(self, N, B, lnut, rnut, lbolt, rbolt):
		if lnut > rnut or lbolt > rbolt:
			return
		if bolt == null:
			p = random.randint(a,b+1)
			B[p],B[b] = B[b],B[p]
		bolt = self.nutBoltPartition(B,a,b)
		nut = self.nutBoltPartition(N,a,b)
		#self.nutBoltSort(
		
	def nutBoltPartition(self, A, a, p):
		l = a
		r = p - 1
		# p = random.int(a,b)
		A[p],A[b] = A[b],A[p]
		while l <= r:
			while A[l] <= p and l <= r:
				l += 1
			while A[r] >= p and r >= l:
				r -= 1
			if l < r:
				A[l],A[r] = A[r],A[l]
		A[l],A[b] = A[b],A[l]
		return l