import collections
def readInput():
	A = []
	with open("data/input6.txt") as f:
		
		A = [ int(x) for x in f.read().split(',')]
			
	return [A]
def solve_part1(A, maxDay):
	day = 0
	fishes = collections.Counter(A)
	while day < maxDay:
		new_fishes = collections.Counter()
		for state in list(fishes.keys()):
			if state == 0:
				new_fishes[8] += fishes[0]
				new_fishes[6] += fishes[0]
			else:
				new_fishes[state-1] += fishes[state]
		fishes = new_fishes
		day += 1
	print (sum(fishes.values()))
def solve_part2(A):
	print (ans)
if __name__ == '__main__':
	input = readInput()
	solve_part1(*input, 80)
	solve_part1(*input, 256)
	

	
