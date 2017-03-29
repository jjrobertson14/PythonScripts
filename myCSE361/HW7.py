import math
import random
import sys

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
		
	def nutBoltSort(self, N, B, low,high):
		if low >= high:
			return
		pNut = random.randint(low, high)
		pBolt = self.nutBoltPartition(B,low,high,N[pNut])
		self.nutBoltPartition(N,low,high,B[pBolt])
		
		self.nutBoltSort(N,B,low,pBolt-1)
		self.nutBoltSort(N,B,pBolt+1,high)
		
	def nutBoltPartition(self, A, low, high, pivot):
		i = low
		r = high - 1
		j = low
		while j < high:
			if A[j] < pivot:
				A[j],A[i] = A[i],A[j]
				i += 1
			elif A[j] == pivot:
				A[j],A[high] = A[high],A[j]
				j -= 1
			j += 1
		A[i],A[high] = A[high],A[i]

		return i