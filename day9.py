import collections
def readInput():
	A = []
	with open("data/input9.txt") as f:
		s = f.readline()
		while s:
			if s[-1] == '\n':
				s = s[:-1]
			new = []
			for c in s:
				new.append(c)
			A.append(new)
			s = f.readline()
	return A
def solve_part1(A):
	ans = 0
	m, n = len(A), len(A[0])
	for i in range(m):
		for j in range(n):
			low = True
			for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
				x, y = i+dx, dy+j
				if x >= 0 and x < m and y >= 0 and y < n:
					if A[x][y] <= A[i][j]:
						low = False
						break
			if low:
				ans += (int(A[i][j])+1)
	print (ans)
def solve_part2(A):
	ans = []
	m, n = len(A), len(A[0])
	def dfs(i, j):
		if A[i][j] == '9':
			return 0
		ans = 1
		A[i][j] = '9'
		for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
			x, y = i+dx, dy+j
			if x >= 0 and x < m and y >= 0 and y < n:
				ans += dfs(x, y)
		return ans
	for i in range(m):
		for j in range(n):
			low = True
			for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
				x, y = i+dx, dy+j
				if x >= 0 and x < m and y >= 0 and y < n:
					if A[x][y] <= A[i][j]:
						low = False
						break
			if low:
				ans.append(dfs(i, j))
	ans.sort()
	print(ans[-1]*ans[-2]*ans[-3])
if __name__ == '__main__':
	input = readInput()
	solve_part1(input)
	solve_part2(input)
	

	
