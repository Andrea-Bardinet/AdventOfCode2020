#!/bin/python3
# -*- coding: UTF-8 -*-

def addMask(val,mask):
	val = str(bin(int(val)))[2:]
	zero = ""
	for i in range(0,len(mask)-len(val)):
		zero += "0"
	val = zero + val
	for i in range(0,len(mask)):
		m = mask[i]
		if m != "X":
			val = val[:i]+m+val[i+1:]
	return int(val,2)

def adrMask(adr,mask):
	adr = str(bin(adr))[2:]
	zero = ""
	for i in range(0,len(mask)-len(adr)):
		zero += "0"
	adr = zero + adr
	for i in range(0,len(mask)):
		m = mask[i]
		if m != "0":
			adr = adr[:i]+m+adr[i+1:]
	nbX = adr.count("X")
	adrs = [adr]
	for i in range(0,nbX):
		temp = []
		for a in adrs:
			temp.append(a.replace("X","0",1))
			temp.append(a.replace("X","1",1))
		adrs = temp
	res = []
	for a in adrs:
		res.append(int(a,2))
	return res
		


input = open("input","r")
lines = input.readlines()


mem = {}

for line in lines:
	line = line[:-1]
	line = line.split(" = ")
	if line[0] == "mask":
		mask = line[1]
	else:
		adr = int(line[0][4:-1])
		val = line[1]
		val = addMask(val,mask)
		mem[adr] = val

part1=0
for i in mem:
	part1 += mem[i]

print("Part1: ",part1)

input.seek(0,0)

mem = {}
for line in lines:
	line = line[:-1]
	line = line.split(" = ")
	if line[0] == "mask":
		mask = line[1]
	else:
		adr = int(line[0][4:-1])
		val = int(line[1])
		for a in adrMask(adr,mask):
			mem[a] = val
		
part2=0
for i in mem:
	part2 += mem[i]

print("Part2: ",part2)