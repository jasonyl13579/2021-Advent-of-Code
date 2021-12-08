import collections
def readInput():
	A = []
	x_max = y_max = 0
	with open("data/input5.txt") as f:
		
		for s in f.readlines():
			temp = s.split(' - ')
			x1, y1 = temp[0].split(',')
			x2, y2 = temp[1].split(',')
			if y2[-1] == '\n': 
				y2 = y2[:-1]
			x_max = x_max if x_max > int(x1) else int(x1)
			x_max = x_max if x_max > int(x2) else int(x2)
			y_max = y_max if y_max > int(y1) else int(y1)
			y_max = y_max if y_max > int(y2) else int(y2)
			A.append(sorted([(int(x1),int(y1)),(int(x2),int(y2))]))
	return A, x_max+1, y_max+1
def solve_part1(A, m, n):
	ans = 0
	board = [[0]*n for _ in range(m)]
	for p1, p2 in A:
		if p1[0] == p2[0]:
			for i in range(p1[1], p2[1]+1):
				board[p1[0]][i] += 1
		if p1[1] == p2[1]:
			for i in range(p1[0], p2[0]+1):
				board[i][p1[1]] += 1
	for i in range(m):
		for j in range(n):
			if board[i][j] >= 2:
				ans += 1
	print (ans)
def solve_part2(A, m, n):
	ans = 0
	board = [[0]*n for _ in range(m)]
	for p1, p2 in A:
		if p1[0] == p2[0]:
			for i in range(p1[1], p2[1]+1):
				board[p1[0]][i] += 1
		elif p1[1] == p2[1]:
			for i in range(p1[0], p2[0]+1):
				board[i][p1[1]] += 1
		elif p1[1] < p2[1]:
			for i in range(p2[0]-p1[0]+1):
				board[p1[0]+i][p1[1]+i] += 1
		else:
			for i in range(p2[0]-p1[0]+1):
				board[p1[0]+i][p1[1]-i] += 1
	for i in range(m):
		for j in range(n):
			if board[i][j] >= 2:
				ans += 1
				
	print (ans)
if __name__ == '__main__':
	input = readInput()
	solve_part1(*input)
	solve_part2(*input)
	

	
