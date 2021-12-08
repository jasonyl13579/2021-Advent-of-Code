with open("data/input1.txt") as f:
	ans = 0
	previous = float('inf')
	for x in f:
		x = int(x)
		if x > previous:
			ans += 1
		previous = x
	print (ans)
	
with open("data/input1.txt") as f:
	ans = 0
	A = []
	for x in f:
		A.append(int(x))
	for i in range(3, len(A)):
		if A[i] > A[i-3]:
			ans += 1
	print (ans)