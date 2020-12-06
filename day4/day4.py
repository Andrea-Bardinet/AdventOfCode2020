#!/bin/python3
# -*- coding: UTF-8 -*-

class Password:
	byr = ""
	iyr = ""
	eyr = ""
	hgt = ""
	hcl = ""
	ecl = ""
	pid = ""
	cid = ""

	def __init__(self, input):
		input = input.split(" ")
		for param in input:
			param = param.split(":")
			if param[0] == "byr":
				self.byr = param[1]
			elif param[0] == "iyr":
				self.iyr = param[1]
			elif param[0] == "eyr":
				self.eyr = param[1]
			elif param[0] == "hgt":
				self.hgt = param[1]
			elif param[0] == "hcl":
				self.hcl = param[1]
			elif param[0] == "ecl":
				self.ecl = param[1]
			elif param[0] == "pid":
				self.pid = param[1]
			elif param[0] == "cid":
				self.cid = param[1]

	def isValidePart1(self):
		if self.byr !="" and self.iyr !="" and self.eyr !="" and self.hgt !="" and self.hcl !="" and self.ecl !="" and self.pid !="":
			return True
		else:
			return False

	def isValidePart2(self):
		if not self.isValidePart1():
			return False

		if not (int(self.byr) >= 1920 and int(self.byr) <= 2002):
			return False
		if not (int(self.iyr) >= 2010 and int(self.iyr) <= 2020):
			return False
		if not (int(self.eyr) >= 2020 and int(self.eyr) <= 2030):
			return False
		if not (self.hgt[-2:] == "cm" or self.hgt[-2:] == "in"):
			return False 
		if self.hgt[-2:] == "cm":
			if not(int(self.hgt[:-2]) >= 150 and int(self.hgt[:-2]) <= 193):
				return False
		if self.hgt[-2:] == "in":
			if not(int(self.hgt[:-2]) >= 59 and int(self.hgt[:-2]) <= 76):
				return False
		if not (self.hcl[0] == '#' and len(self.hcl[1:]) == 6):
			return False
		for c in self.hcl[1:]:
			if "abcdef0123456789".count(c) == 0:
				return False
		if not (self.ecl=="amb" or self.ecl=="blu" or self.ecl=="brn" or self.ecl=="gry" or self.ecl=="grn" or self.ecl=="hzl" or self.ecl=="oth"):
			return False
		print(self.pid)
		if not (len(self.pid) == 9):
			return False
		return True





input = open("input","r")
lines = input.readlines()

part1 = 0
part2 = 0
s = ""
for l in lines:
	if l != "\n":
		s = s + " " + l[:-1]
	else:
		p = Password(s[1:])
		if p.isValidePart1():
			part1 = part1 + 1
		if p.isValidePart2():
			part2 = part2 + 1
		s = ""

print("Part1: " + str(part1))
print("Part2: " + str(part2))