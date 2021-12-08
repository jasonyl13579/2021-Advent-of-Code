import collections
with open("data/input3.txt") as f:
	A = []
	for x in f:
		A.append(x)
	n = len(A[0])-1
	
	count = [[0]*n for i in range(2)]
	for x in A:
		for i in range(n):
			count[int(x[i])][i] += 1
	gamma = epsilon = 0
	i = n-1
	for x, y in zip(*count):
		if x >= y:
			epsilon += 1 << i
		else:
			gamma += 1 << i
		i -= 1
	print (gamma, epsilon)
	print (gamma*epsilon)
	
with open("data/input3.txt") as f:
	A = []
	for x in f:
		A.append(x)
	n = len(A[0])-1
	o2 = set(A)
	co2 = set(A)
	i = 0
	while i < n:
		if len(o2) != 1:
			zero = one = 0
			for x in o2:
				zero += int(x[i]) == 0
				one += int(x[i]) == 1
			for x in list(o2):
				if (one >= zero and x[i] == '0') or (one < zero and x[i] == '1'):
					o2.remove(x)
		if len(co2) != 1:
			zero = one = 0
			for x in co2:
				zero += int(x[i]) == 0
				one += int(x[i]) == 1
			#print (zero, one)
			for x in list(co2):
				if (one >= zero and x[i] == '1') or (one < zero and x[i] == '0'):
					co2.remove(x)
		if len(o2) == 1 and len(co2) == 1:
			break
		i += 1
	
	x = y = 0
	print (o2,co2)
	for i in range(n):
		x += int(list(o2)[0][i]) << (n-i-1)
		y += int(list(co2)[0][i]) << (n-i-1)
	print (x*y)
	'''
	for x in A:
		for i in range(n):
			count[int(x[i])][i] += 1
	gamma = epsilon = 0
	i = n-1
	for x, y in zip(*count):
		if x >= y:
			epsilon += 1 << i
		else:
			gamma += 1 << i
		i -= 1
	'''