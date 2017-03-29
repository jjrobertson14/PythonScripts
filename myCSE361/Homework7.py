#!/bin/python
import math

class Homework7():

	def __init__(self):
		self.ops = 0

	def resetOps(self):
		self.ops = 0

	def colorSort(self, A, red, blue, green):
		#colors are numbers defined on call
		s = 0
		e = len(A) - 1
		m = int(math.floor(e / 2))
	
		while (s < m):
			if (A[s] == green):
				while (A[m] == green):
					m = m + 1
					if (m + 1 = len(A)):
						while (A[m] == green):
							m -= 1
				A[s],A[m] = A[m],A[s]
			if(A[e] == green):
				while (A[m] == green):
					m = (m - 1) % len(A)
					if (m + 1 = len(A)):
                                                while (A[m] == green):
                                                        m -= 1
				A[e],A[m] = A[m],A[e]

			elif (A[s] == red):
				if (A[e] == blue):
					A[s],A[e] = blue,red
					s += 1
					e -= 1
				elif (A[e] == red):
					e -= 1
			elif (A[s] == blue):
				s += 1
				if(A[e] == red):
					e -= 1
		while (e > m):
			if (A[e] == blue):
				A[s+1],A[e] = A[e],A[s+1]
				lastGreen = e
				e -= 1
			if (A[e] == red):
				A[e],A[lastGreen] = A[lastGreen],A[e]
		print('s=' + str(s) + ' m=' + str(m) + ' e=' + str(e))
