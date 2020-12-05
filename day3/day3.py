#!/bin/python3
# -*- coding: UTF-8 -*-

input = open("input","r")

mod = 31


def countTree(slopeX, slopeY, input):
	input.seek(0, 0)
	lines = input.readlines()
	tree = 0
	pos = 0
	pause = 1

	for l in lines:
		if pause == 1:
			l = l[:-1]
			if l[pos] == '#':
				tree = tree + 1

			pos = pos + slopeX
			pos = pos % mod
			pause = slopeY
		else:
			pause = pause - 1
			
	return tree


a = countTree(3,1,input)
print("Part1: "+str(a))

a *= countTree(1,1,input)
a *= countTree(5,1,input)
a *= countTree(7,1,input)
a *= countTree(1,2,input)

print("Part2: "+str(a))





