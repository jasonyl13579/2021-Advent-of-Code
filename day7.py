import collections
def readInput():
	A = []
	with open("data/input7.txt") as f:
		
		A = [ int(x) for x in f.read().split(',')]
			
	return [A]
def solve_part1(A):
	A.sort()
	n = len(A)
	fp = A[n//2]
	print (sum([abs(x-fp) for x in A]))
def solve_part2(A):
	ans = float('inf')
	maxA, minA = max(A), min(A)
	for i in range(minA, maxA+1):
		cost = 0
		for j in A:
			x = abs(j-i)
			cost += (1+x)*x/2
		ans = min(ans, cost)
	print (ans)
if __name__ == '__main__':
	input = readInput()
	solve_part1(*input)
	solve_part2(*input)
	

	
