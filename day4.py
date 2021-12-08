import collections
def checkbingo(x, y, board, a):
	if board[0][y] in a and board[1][y] in a and board[2][y] in a and board[3][y] in a and board[4][y] in a:
		return sum([board[i][y] for i in range(5)])
	if board[x][0] in a and board[x][1] in a and board[x][2] in a and board[x][3] in a and board[x][4] in a:
		return sum(board[x])
	#if x == y and board[0][0] in a and board[1][1] in a and board[2][2] in a and board[3][3] in a and board[4][4] in a:
	#	return sum([board[i][i] for i in range(5)])
	#if x+y == 4 and board[0][4] in a and board[1][3] in a and board[2][2] in a and board[3][1] in a and board[4][0] in a:
	#	return sum([board[i][4-i] for i in range(5)])
	return 0
with open("data/input4.txt") as f:
	A = []
	A = [int(i) for i in f.readline()[:-1].split(',')]
	boards = []
	
	while f.readline():
		board = []
		for _ in range(5):
			line = f.readline()
			if line[-1] == '\n':
				line = line[:-1]
			nums = line.split(' ')
			x = []
			for n in nums:
				if n != '':
					x.append(int(n))
			board.append(x)
		boards.append(board)
	
	n = len(boards)
	boards_dict = []
	for i in range(n):
		board = {}
		for j in range(5):
			for k in range(5):
				board[boards[i][j][k]] = (j,k) 
		boards_dict.append(board)
	
	round = 0
	ans = 0
	appeared = set()
	end = 0
	while round < len(A):
		num = A[round]
		appeared.add(num)
		if round >= 5:
			for i, board in enumerate(boards_dict):
				if num in board:
					x, y = board[num]
					win = checkbingo(x, y, boards[i], appeared)
					if win:
						for j in range(5):
							for k in range(5):
								if boards[i][j][k] not in appeared:
									ans += boards[i][j][k]
						end = 1
						break
		if end: 
			break
		round += 1
	print (ans, A[round])
	print (ans* A[round])

with open("input4.txt") as f:
	A = []
	A = [int(i) for i in f.readline()[:-1].split(',')]
	boards = []
	
	while f.readline():
		board = []
		for _ in range(5):
			line = f.readline()
			if line[-1] == '\n':
				line = line[:-1]
			nums = line.split(' ')
			x = []
			for n in nums:
				if n != '':
					x.append(int(n))
			board.append(x)
		boards.append(board)
	
	n = len(boards)
	boards_dict = []
	for i in range(n):
		board = {}
		for j in range(5):
			for k in range(5):
				board[boards[i][j][k]] = (j,k) 
		boards_dict.append(board)
	
	round = 0
	ans = 0
	end = 0
	appeared = set()
	notfinished = set([i for i in range(n)])
	while round < len(A):
		num = A[round]
		appeared.add(num)
		if round >= 5:
			for i in list(notfinished):
				board = boards_dict[i]
				if num in board:
					x, y = board[num]
					win = checkbingo(x, y, boards[i], appeared)
					if win:
						if len(notfinished) == 1:
							for j in range(5):
								for k in range(5):
									if boards[i][j][k] not in appeared:
										ans += boards[i][j][k]
							end = 1
							break
						notfinished.remove(i)
		if end:
			break
		round += 1
	print (ans, A[round])
	print (ans* A[round])

	
	

	
