#!/bin/python3
# -*- coding: UTF-8 -*-
#	 N
#	E W
#	 S


class Facing:
	def __init__(self):
		self.pos = ["E","N","W","S"]
		self.face = 0

	def getFace(self):
		return self.pos[self.face]

	def turnLeft(self):
		self.face += 1
		self.face = self.face % 4

	def turnRight(self):
		self.face -= 1
		self.face = self.face % 4

	def setFace(self,pos):
		for i in range(0,4):
			if self.pos[i] == pos:
				self.face = i

class Ship:
	def __init__(self):
		self.facing = Facing()
		self.coord = {'E':0,'N':0,'W':0,'S':0}
		self.waypoint = {'E':10,'N':1,'W':0,'S':0}

	def waypointTurnLeft(self):
		w = self.waypoint
		newWaypoint = {'E':w['S'],'N':w['E'],'W':w['N'],'S':w['W']}
		self.waypoint = newWaypoint

	def waypointTurnRight(self):
		w = self.waypoint
		newWaypoint = {'E':w['N'],'N':w['W'],'W':w['S'],'S':w['E']}
		self.waypoint = newWaypoint


	def do1(self,line):
		action = line[0]
		number = int(line[1:])
		if action == "F":
			self.coord[self.facing.getFace()] += number
		elif action == "L" or action == "R":
			rot = int(number/90)
			for i in range(0,rot):
				if action == "L":
					self.facing.turnLeft()
				else:
					self.facing.turnRight()
		else:
			self.coord[action] += number

	def do2(self,line):
		action = line[0]
		number = int(line[1:])
		if action == "F":
				for c in self.waypoint:
					self.coord[c] += self.waypoint[c]*number
		elif action == "L" or action == "R":
			rot = int(number/90)
			for i in range(0,rot):
				if action == "L":
					self.waypointTurnLeft()
				else:
					self.waypointTurnRight()
		else:
			self.waypoint[action] += number
		


	def getDistance(self):
		res = abs(self.coord['E']-self.coord['W'])
		res+= abs(self.coord['N']-self.coord['S'])
		return res





input = open("input","r")
lines = input.readlines()

ship1 = Ship()
for line in lines:
	line = line[:-1]
	ship1.do1(line)
part1 = ship1.getDistance()
print("Part1: ",str(part1))

input.seek(0,0)
ship2 = Ship()
for line in lines:
	line = line[:-1]
	ship2.do2(line)
part2 = ship2.getDistance()
print("Part2: ",str(part2))
