#!/bin/python3
# -*- coding: UTF-8 -*-

input = open("input","r")
input = input.readlines()

part1 = 0
part2 = 0

for l in input:
	#input fragmentation
	l = l.split("-")
	x1 = int(l[0])
	l = l[1].split(" ")
	x2 = int(l[0])
	char = l[1][0]
	string = l[2][:-1]
	nbChar = string.count(char)

	#answer for part1
	if(nbChar >=  x1 and nbChar <= x2):
		part1 = part1 + 1

	#answer for part2
	if((string[x1-1] == char) ^ (string[x2-1] == char)):
		part2 = part2 + 1

print("part1: "+str(part1))
print("part2: "+str(part2))