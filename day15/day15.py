#!/bin/python3
# -*- coding: UTF-8 -*-

input = "16,1,0,18,12,14,19"
endTurn = 30000000

numbers = dict()
turn = 1
for n in input.split(","):
	numbers[int(n)] = [turn,turn]
	last = int(n)
	turn+=1


new=True
for turn in range(turn,endTurn+1):
	if new:
		last=0
	else:
		last = numbers[last][1] - numbers[last][0]

	if last in numbers:
		new=False
		numbers[last][0] = numbers[last][1]
		numbers[last][1] = turn
	else:
		new=True
		numbers[last] = [turn,turn]


print("Answer: "+str(last))




