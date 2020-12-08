#!/bin/python3
# -*- coding: UTF-8 -*-

class Bag:

	def __init__(self, color):
		self.color = color
		self.contain = []

	def addContain(self, bag, quantite):
		self.contain.append([bag,quantite])

	def getColor(self):
		return self.color

	def __str__(self):
		s = "["+self.color+"]:"
		for c in self.contain:
			s+= c[1] +" "+ c[0].getColor() + ", "
		return s

	def isContainShiny(self):
		for c in self.contain:
			bag = c[0]
			if bag.getColor() == "shiny gold":
				return True
			elif bag.isContainShiny():
				return True
		return False

	def countBagsInside(self):
		res = 0
		for c in self.contain:
			bag = c[0]
			nbBag = c[1]
			res += int(nbBag)
			res += bag.countBagsInside() * int(nbBag)
		return res


		

input = open("input","r")
lines = input.readlines()

bags = []

for l in lines:
	l = l[:-2]
	l = l.split("bags contain")
	l[0] = l[0][:-1]
	b = Bag(l[0])
	bags.append(b)

input.seek(0,0)

for l in lines:
	l = l[:-2]
	l = l.split("bags contain")
	color1 = l[0]
	color1 = color1[:-1]
	l = l[1].split(",")
	
	for bag in bags:
		if bag.getColor() == color1:
			b1 = bag

	for b in l:
		b = b[1:].split(" ")
		color2 = b[1]+" "+b[2]

		find = False
		for bag in bags:
			if bag.getColor() == color2:
				b2 = bag
				find = True
		if find:
			b1.addContain(b2,b[0])
		

part1 = 0
part2 = 0


for bag in bags:
	shiny =  bag.isContainShiny()
	if shiny:		
		part1 += 1
	if bag.getColor() == "shiny gold":
		part2 = bag.countBagsInside()

print("Part1: "+str(part1))
print("Part2: "+str(part2))