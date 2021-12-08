import collections
def readInput():
	pattern = []
	code = []
	with open("data/input8.txt") as f:
		s = f.readline()
		while s:
			if s[-1] == '\n':
				s = s[:-1]
			x = s.split(' | ')
			pattern.append(x[0].split(' '))
			code.append(x[1].split(' '))
			s = f.readline()
			
	return pattern, code
def solve_part1(pattern, code):
	ans = 0
	for c in code:
		for s in c:
			if len(s) in {2,4,3,7}:
				ans +=1
	print (ans)
def solve_part2(pattern, code):
	ans = 0
	for C, P in zip(code, pattern):
		used = set()
		code_ans = [-1]*4
		answer = [0]*10
		patterns = [set(x) for x in P]
		codes = [set(x) for x in C]
		for p in patterns:
			if len(p) == 2:
				answer[1] = p
				used.add(''.join(sorted([x for x in p])))
			if len(p) == 4:
				answer[4] = p
				used.add(''.join(sorted([x for x in p])))
			if len(p) == 3:
				answer[7] = p
				used.add(''.join(sorted([x for x in p])))
			if len(p) == 7:
				answer[8] = p
				used.add(''.join(sorted([x for x in p])))
		# solve 9
		for p in patterns:
			if len(p) == 6 and len(p&answer[4]) == 4 and ''.join(sorted([x for x in p])) not in used:
				answer[9] = p
				used.add(''.join(sorted([x for x in p])))
				break
		# solve 0
		for p in patterns:
			if len(p) == 6 and len(p&answer[1]) == 2 and ''.join(sorted([x for x in p])) not in used:
				answer[0] = p
				used.add(''.join(sorted([x for x in p])))
				break
		# solve 6
		for p in patterns:
			if len(p) == 6 and ''.join(sorted([x for x in p])) not in used:
				answer[6] = p
				used.add(''.join(sorted([x for x in p])))
				break
		# solve 3
		for p in patterns:
			if len(p) == 5 and len(p & answer[1]) == 2 and ''.join(sorted([x for x in p])) not in used: 
				answer[3] = p
				used.add(''.join(sorted([x for x in p])))
				break	
		# solve 5
		for p in patterns:
			if len(p&answer[9]) == 5 and ''.join(sorted([x for x in p])) not in used:
				answer[5] = p
				used.add(''.join(sorted([x for x in p])))
				break
		# solve 2
		for p in patterns:
			if ''.join(sorted([x for x in p])) not in used:
				answer[2] = p
				break
		
		for i, c in enumerate(codes):
			for j, p in enumerate(answer):
				if c == p:
					code_ans[i] = j
					break
		#print (used)
		#print (code_ans, answer)
		code_int = int(''.join([str(i) for i in code_ans]))
		ans += code_int
		#print (code_int)
		
	print (ans)
def setToStr(A):
	return ''.join(sorted([x for x in A]))
if __name__ == '__main__':
	input = readInput()
	solve_part1(*input)
	solve_part2(*input)
	

	
