#!/bin/python3
# -*- coding: UTF-8 -*-

class Instruction:

	def __init__(self):
		self.action = ""
		self.value = 0

	def getAction(self):
		return self.action

	def setAction(self, action):
		self.action = action

	def getValue(self):
		return self.value

	def setValue(self, value):
		self.value = value

	def readInstruction(self, string):
		string = string.split(" ")
		self.setAction(string[0])
		self.setValue(int(string[1]))

	def inversAction(self):
		if self.getAction() == "jmp":
			self.setAction("nop")
		elif self.getAction() == "nop":
			self.setAction("jmp")

	def __str__(self):
		return "Action: "+self.getAction()+"   Value: "+str(self.getValue())



class Game:
	
	def __init__(self):
		self.acc = 0
		self.instruction = []
		self.pos = 0
		self.end = 0

	def getAcc(self):
		return self.acc
	
	def setAcc(self, value):
		self.acc = self.getAcc() + value

	def resetAcc(self):
		self.acc = 0

	def getPos(self):
		return self.pos

	def setPos(self, value):
		self.pos = self.getPos() + value

	def resetPos(self):
		self.pos = 0

	def getEnd(self):
		return self.end

	def isEnd(self):
		if self.getPos() == self.getEnd():
			return True
		return False

	def setEnd(self, end):
		self.end = end

	def getInstruction(self):
		self.instruction[self.getPos()][1] = True
		return self.instruction[self.getPos()][0]

	def addInstruction(self, instruction):
		self.instruction.append([instruction,False])
		self.end = self.getEnd() + 1

	def runInstruction(self, i):
		action = i.getAction()
		value = i.getValue()
		if action == "acc":
			self.setAcc(value)
			self.setPos(1)
		elif action == "jmp":
			self.setPos(value)
		elif action == "nop":
			self.setPos(1)

	def resetVisite(self):
		for i in self.instruction:
			i[1] = False

	def isVisited(self):
		return self.instruction[self.getPos()][1]

	def resetParam(self):
		self.resetPos()
		self.resetAcc()
		self.resetVisite()

	def runGame(self):
		self.resetParam()
		while not self.isEnd():
			self.runInstruction(self.getInstruction())

	def runBrokeGame(self):
		self.resetParam()
		while not self.isVisited():
			self.runInstruction(self.getInstruction())

	def isGameOk(self):
		self.resetParam()
		while not self.isEnd():
			if self.isVisited():
				return False
			self.runInstruction(self.getInstruction())
		return True

	def resolveGame(self):
		for tab in self.instruction:
			i = tab[0]
			i.inversAction()
			if self.isGameOk():
				return True
			i.inversAction()
		return False

	def __str__(self):
		s = "Acc:"+str(self.getAcc())
		s += "   "
		s += "Pos:"+str(self.getPos())
		return s



input = open("input","r")
lines = input.readlines()

game = Game()

for line in lines:
	i = Instruction()
	i.readInstruction(line[:-1])
	game.addInstruction(i)


game.runBrokeGame()
print("Part1: "+str(game.getAcc()))


game.resolveGame()
game.runGame()
print("Part2: "+str(game.getAcc()))


