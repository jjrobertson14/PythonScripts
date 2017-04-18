import sys

L = [0,23,59,17,47,14,40,22,8]
Sol = []
Q = []
target = int(sys.argv[1])

for i in range(0,len(L)):
	Q.append([])
	for j in range(0,target+1):
		Q[i].append([])

for s in range(0,target+1):
	Q[1][s] = L[1] == s
	#print thing
	
for i in range (2,len(L)):
	s = 0
	while s <= target:
		if (s - L[i] >= 0):
			Q[i][s] = (bool(Q[i-1][s]) or L[i] == s or bool(Q[i-1][s-L[i]]))
		else:
			Q[i][s] = (bool(Q[i-1][s]) or L[i] == s) 
		if bool(Q[i-1][s-L[i]]) == True:
			Sol.append(L[i])
		s += 1
		
for row in range(0,len(Q)):
	for col in range (0,len(Q[row])):
		#if bool(Q[row][col]):
		print (str(row) + " " + str(col) + "\t" + str(Q[row][col]))
		#print str(len(Q[row]))

i = 8
s = target
while s > 0:
	if Q[i][s] == True and Sol.__contains__(L[i]):
		print str(L[i])
		i -= 1
		s -= L[i]
	elif Q[i-1][s] == True:
		print str(L[i-1])
		i-=1
	else:
		s-=1