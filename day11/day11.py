#!/bin/python3
# -*- coding: UTF-8 -*-


class Seat:

	def __init__(self,etat):
		self.occupe = etat

	def isOccupe(self):
		return self.occupe

	def setOccupe(self, etat):
		self.occupe = etat

	def __str__(self):
		if self.isOccupe():
			return "#"
		return "L"

	def equals(self, seat):
		return self.isOccupe() == seat.isOccupe()
		

class Case:

	def __init__(self, forme):
		if forme == None:
			self.forme = "floor"
		else:
			self.forme = "seat"
			self.seat = forme

	def getForme(self):
		return self.forme

	def getSeat(self):
		if self.getForme() == "floor":
			return None
		return self.seat

	def __str__(self):
		if self.getForme() == "floor":
			return(".")
		else:
			return(self.getSeat().__str__())

	def equals(self, case):
		if case.getForme() == self.getForme():
			if self.getForme() == "seat":
				return self.getSeat().equals(case.getSeat())
			else:
				return True

class Matrice:

	def __init__(self, input):
		lines = input.readlines()
		self.matrice = []
		for line in lines:
			tab = []
			line = line[:-1]
			for char in line:
				if char == 'L':
					case = Case(Seat(False))
				elif char == '#':
					case = Case(Seat(True))
				else:
					case = Case(None)
				tab.append(case)
			self.matrice.append(tab)
		self.x = len(self.matrice[0])
		self.y = len(self.matrice)

	def equals(self, matrice):
		for i in range(0,self.y):
			for j in range(0,self.x):
				if not self.matrice[i][j].equals(matrice[i][j]):
					return False
		return True

	def roundPart1(self):
		newMatrice = []
		for i in range(0,self.y):
			tab = []
			for j in range(0, self.x):
				case = self.matrice[i][j]
				if case.getForme() == "seat":
					countOccupe = 0
					for a in range(-1,2):
						for b in range(-1,2):
							x = b+j
							y = a+i							
							if x>=0 and x<self.x and y>=0 and y<self.y and not(x==j and y==i):
								if self.matrice[y][x].getForme() == "seat":
									if self.matrice[y][x].getSeat().isOccupe():
										countOccupe+=1
					if countOccupe >= 4:
						tab.append(Case(Seat(False)))
					elif countOccupe == 0 and not case.getSeat().isOccupe():
						tab.append(Case(Seat(True)))
					else:
						tab.append(Case(Seat(case.getSeat().isOccupe())))
				else:
					tab.append(Case(None))
			newMatrice.append(tab)
		return newMatrice

	def getLine(self,x,y,a,b):
		tab = []
		x+=a
		y+=b
		while x>=0 and x<self.x and y>=0 and y<self.y:
			tab.append(self.matrice[y][x])
			x+=a
			y+=b
		return tab

	def countSee(self,x,y):
		way = []
		res = 0
		for a in range(-1,2):
			for b in range(-1,2):
				if not (a==0 and b==0):
					way.append(self.getLine(x,y,a,b))
		for tab in way:
			see = False
			occupe = False
			for case in tab:
				if not see:
					if case.getForme() == "seat":
						see = True
						if case.getSeat().isOccupe():
							occupe = True			
			if occupe:
				res+=1
		return res



	def roundPart2(self):
		newMatrice = []
		for i in range(0,self.y):
			tab = []
			for j in range(0, self.x):
				case = self.matrice[i][j]
				if case.getForme() == "seat":
					countOccupe = self.countSee(j,i)
					if countOccupe >= 5:
						tab.append(Case(Seat(False)))
					elif countOccupe == 0 and not case.getSeat().isOccupe():
						tab.append(Case(Seat(True)))
					else:
						tab.append(Case(Seat(case.getSeat().isOccupe())))
				else:
					tab.append(Case(None))
			newMatrice.append(tab)
		return newMatrice


	def copyMatrice(self):
		res = []
		for tab in self.matrice:
			resTab = []
			for i in tab:
				resTab.append(i)
			res.append(resTab)
		return res

	def runUntilStuckPart1(self):
		newMatrice = self.roundPart1()
		while(not self.equals(newMatrice)):
			self.matrice = newMatrice
			newMatrice = self.roundPart1()

	def runUntilStuckPart2(self):
		newMatrice = self.roundPart2()
		while(not self.equals(newMatrice)):
			self.matrice = newMatrice
			newMatrice = self.roundPart2()

	def countOccupe(self):
		res = 0
		for tab in self.matrice:
			for c in tab:
				if c.getForme() == "seat":
					if c.getSeat().isOccupe():
						res += 1
		return res

	def __str__(self):
		s = ""
		for tab in self.matrice:
			for case in tab:
				s+= case.__str__()
			s+="\n"
		return s



input = open("input","r")

print("Sorry, it will take a little while :'(")

matrice = Matrice(input)
matrice.runUntilStuckPart1()
part1 = matrice.countOccupe()
print("Part1: ",str(part1))

input.seek(0,0)
matrice = Matrice(input)
matrice.runUntilStuckPart2()
part2 = matrice.countOccupe()
print("Part2: ",str(part2))