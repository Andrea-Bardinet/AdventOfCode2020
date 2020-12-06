#!/bin/python3
# -*- coding: UTF-8 -*-

letters = "abcdefghijklmnopqrstuvwxyz"

class Personne:

	def __init__(self,string):
		self.answer = string

	def getAnswer(self):
		return self.answer

class Groupe:

	def __init__(self):
		self.personnes = []

	def addPersonne(self, personne):
		self.personnes.append(personne)

	def nbPersonne(self):
		return self.personnes.count()

	def part1(self):
		yes = 0

		s = ""
		for p in self.personnes:
			s+=p.getAnswer()

		for l in letters:
			if s.count(l) > 0:
				yes += 1

		return yes

	def part2(self):
		yes = 0
		isYes = []

		for x in range(0,26):
			isYes.append(True)
			for p in self.personnes:
				if p.getAnswer().count(letters[x]) == 0:
					isYes[x] = False
					
		return isYes.count(True)



input = open("input","r")
lines = input.readlines()
lines.append("\n")


personnes = []
groupes = []

for l in lines:
	l = l[:-1]
	if l != "":
		personnes.append(Personne(l))
	else:
		g = Groupe()
		for p in personnes:
			g.addPersonne(p)
		groupes.append(g)
		personnes = []


part1 = 0
part2 = 0

for g in groupes:
	part1 += g.part1()
	part2 += g.part2()


print("Part1: "+str(part1))
print("Part2: "+str(part2))