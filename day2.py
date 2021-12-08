with open("data/input2.txt") as f:
	horizontal = depth = 0
	instruction = []
	for x in f:
		instruction.append(x.split(' '))
	for commend, n in instruction:
		n = int(n)
		if commend == 'forward':
			horizontal += n
		elif commend == 'down':
			depth += n
		else:
			depth -= n
	print (depth*horizontal)
	
with open("data/input2.txt") as f:
	horizontal = depth = aim = 0
	instruction = []
	for x in f:
		instruction.append(x.split(' '))
	for commend, n in instruction:
		n = int(n)
		if commend == 'forward':
			horizontal += n
			depth += (aim*n)
		elif commend == 'down':
			aim += n
		else:
			aim -= n
	print (depth*horizontal)
	