#!/bin/python3
# -*- coding: UTF-8 -*-

import itertools
import numpy

def isCorrect(inp):
	last = inp[0]-1
	for i in inp:
		if not (i > last and i <= last + 3):
			return False
		last = i
	return True

def listToArray(l):
	res = []
	for i in l:
		res.append(i)
	return res


input = open("input","r")
lines = input.readlines()

jolts = []

for line in lines:
	line = line[:-1]
	jolts.append(int(line))

jolts.insert(0,0)
jolts.append(max(jolts)+3)
jolts.sort()

jolt1 = 0
jolt3 = 0
last = 0

for i in jolts:
	if i == last + 1:
		jolt1 += 1
	elif i == last + 3:
		jolt3 += 1
	last = i

part1 = jolt1 * jolt3

print("Part1: "+str(part1))


tabJolts = []
last = 0
lastI = 0
for i in range(0,len(jolts)):
	if jolts[i] == last + 3:
		tabJolts.append(jolts[lastI:i+1])
		lastI = i
	last = jolts[i]



nt = []
for i in tabJolts:
	if len(i) > 2:
		nt.append(i)
tabJolts = nt



part2 = 1
for tab in tabJolts:
	current = 0
	mini = tab[0]
	maxi = tab[len(tab)-1]
	tab = tab[1:-1]
	for lenght in range(1,len(tab)+1):
		combi = list(itertools.combinations(tab,lenght))
		for i in combi:
			i = listToArray(i)
			i.insert(0,mini)
			i.append(maxi)
			if(isCorrect(i)):
				current +=1
	part2 *= current


print("Part2: ",str(part2))

		


