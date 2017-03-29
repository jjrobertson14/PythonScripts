import math
import sys

class BoundBox:
	def __init__(self):
		self.numComps = 0

	def resetComps(self):
		self.numComps = 0

	def bound(self, S):
		if len(S) > 2:
			for i in S:
				sys.stdout.write(str(i) + " ")
			sys.stdout.write('\n')
			m = int((len(S))/2)
			e = int(len(S))
			opt1 = self.bound(S[0:m])
			opt2 = self.bound(S[m:e])
			
			self.numComps += 1
			if opt1[0] < opt2[0]:
				min = opt1[0]
			else:
				min = opt2[0]
			
			self.numComps += 1
			if opt1[1] > opt2[1]:
				max = opt1[1]
			else:
				max = opt2[1]
			return [min,max]
		else:
			#for i in S:
			#	sys.stdout.write(str(i) + " ")
			#sys.stdout.write('\n')
			
			self.numComps += 1
			if S[0] < S[int(len(S)-1)]:
				return [S[0],S[len(S)-1]]
			return [S[int(len(S)-1)],S[0]]
			#return [S[0],S[0]]
			
	def slowBound(self, S):
		print ("HELLO")
		smol = 999999
		lorg = 0
		for i in S:
			self.numComps += 2
			if(i < smol):
				smol = i
			if(i > lorg):
				lorg = i
		return [smol,lorg]
				