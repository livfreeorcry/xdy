import re
from random import randint

def parseRoll(rollString):
	numDice = 1
	plus = 0
	regex = r'^[0-9]{,2}[dD][1-9][0-9]?([\+ p][0-9]{1,5})?$'
	if not re.match(regex,rollString):
		raise ValueError('Invalid roll string: %s' %(rollString))
	splitString = re.split(r'[d\+ ]+',rollString)
	if len(splitString)==3 and splitString[0] != '':
		numDice, die, plus = splitString
	elif len(splitString)==3 and splitString[0] == '':
		blank, die, plus = splitString
	elif len(splitString)==2 and splitString[0] != '':
		numDice, die = splitString
	else:
		die=splitString[1]
	return int(numDice), int(die), int(plus)

class Roll(object):
	def __init__(self, sides=6, ammount=1, plus=0):
		self.sides=sides
		self.ammount=ammount
		self.plus=plus
		# self.rollString = "%dd%d+%d"%(self.ammount, self.sides, self.plus) if (plus != 0) else "%dd%d"(self.ammount, self.sides)
		self.rollString = "ugh"
		self.results=[]

	@classmethod
	def from_string(cls, rollString):
		rollString=rollString
		ammount, sides, plus = parseRoll(rollString)
		return cls(ammount,sides,plus)

	def throw(self):
		for i in range(self.ammount):
			self.results.append(randint(1,self.sides))
		return self.results
		
	def roll(self):
		throw = self.throw()
		return sum(throw)+self.plus

	def __str__(self):
		return '['+','.join(map(str,self.results))+']' if self.results else '['+','.join(map(str,self.throw()))+']'

	def __int__(self):
		return sum(self.results)+self.plus if self.results else sum(self.throw())+self.plus