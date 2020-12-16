#!/bin/python3
# -*- coding: UTF-8 -*-

import os

input = open("input","r")
lines = input.readlines()


bus = []
tabPart2 = []
timestamp = int(lines[0][:-1])
for i in lines[1].split(","):
	tabPart2.append(i)
	if i != "x":
		bus.append(int(i))

waitBus = {}
for i in bus:
	wait = i
	while wait<=timestamp:
		wait +=i
	waitBus[i] = wait


part1 = 0
mini = waitBus[bus[0]]
for i in waitBus:
	if waitBus[i] <= mini:
		mini = waitBus[i]
		part1 = i*(waitBus[i]-timestamp)

print("Part1: ",str(part1))


t = 0
bus=[]
for i in tabPart2:
	if i != "x":
		bus.append([int(i),t])
	t+=1




time = 0
inc = 1
for b in bus:
	while True:
		if (time + b[1]) % b[0] == 0:
			part2 = time
			break
		time += inc
	inc *= b[0]

print("Part2: "+str(part2))

   

