import collections
def readInput():
	A = []
	with open("data/input10.txt") as f:
		s = f.readline()
		while s:
			if s[-1] == '\n':
				s = s[:-1]
			A.append(s)
			s = f.readline()
	return A
point = {')': 3, ']':57, '}':1197, '>':25137}
def solve_part1(A):
	ans = 0
	for s in A:
		stack = []
		for c in s:
			if c == '{' or c == '(' or c == '[' or c == '<':
				stack.append(c)
			else:
				if c == '}':
					if not stack or stack[-1] != '{':
						ans += point[c]
						break
					if stack:
						stack.pop()
				if c == ']':
					if not stack or stack[-1] != '[':
						ans += point[c]
						break
					if stack:
						stack.pop()
				if c == ')':
					if not stack or stack[-1] != '(':
						ans += point[c]
						break
					if stack:
						stack.pop()
				if c == '>':
					if not stack or stack[-1] != '<':
						ans += point[c]
						break
					if stack:
						stack.pop()

	print (ans)
point2 = {'(': 1, '[':2, '{':3, '<':4}
def solve_part2(A):
	ans = 0
	scores = []
	for s in A:
		stack = []
		corrupted = False
		for c in s:
			if c == '{' or c == '(' or c == '[' or c == '<':
				stack.append(c)
			else:
				if c == '}':
					if stack and stack[-1] != '{':
						corrupted = True
						break
					if stack:
						stack.pop()
				if c == ']':
					if stack and stack[-1] != '[':
						corrupted = True
						break
					if stack:
						stack.pop()
				if c == ')':
					if stack and stack[-1] != '(':
						corrupted = True
						break
					if stack:
						stack.pop()
				if c == '>':
					if stack and stack[-1] != '<':
						corrupted = True
						break
					if stack:
						stack.pop()
		if not corrupted:
			score = 0 
			while stack:
				c = stack.pop()
				score *= 5
				score += point2[c]
			scores.append(score)
		scores.sort()
	print (scores[len(scores)//2])
	
if __name__ == '__main__':
	input = readInput()
	solve_part1(input)
	solve_part2(input)
	

	
