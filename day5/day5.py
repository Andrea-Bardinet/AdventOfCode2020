#!/bin/python3
# -*- coding: UTF-8 -*-

input = open("input","r")
lines = input.readlines()

part1 = 0
seat = []

for l in lines:
	l = l[:-1]
	b1 = l[:-3].replace("F","0")
	b1 = b1.replace("B","1")
	b2 = l[-3:].replace("L","0")
	b2 = b2.replace("R","1")

	b1 = int(b1,2)
	b2 = int(b2,2)

	ans = b1*8 + b2
	seat.append(ans)

	if ans > part1:
		part1 = ans

print("Part1: "+str(part1))
	
seat.sort()
a = 0
for s in seat:
	if a != 0:
		if s == a+2:
			part2 = s-1
	a = s

print("Part2: "+str(part2))