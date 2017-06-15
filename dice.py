import re
from random import randint

def parseRoll(rollString):
	ammount = 1
	plus = 0
	regex = r'^[0-9]{,2}[dD][1-9][0-9]?([\+ p][0-9]{1,5})?$'
	if not re.match(regex,rollString):
		raise ValueError('Invalid roll string: %s' %(rollString))
	splitString = re.split(r'[dD\+ p]+',rollString)
	if len(splitString)==3 and splitString[0] != '':
		ammount, sides, plus = splitString
	elif len(splitString)==3 and splitString[0] == '':
		blank, sides, plus = splitString
	elif len(splitString)==2 and splitString[0] != '':
		ammount, sides = splitString
	else:
		sides=splitString[1]
	return int(ammount), int(sides), int(plus)

def parseString(rollString):
	baseroll = re.match(r'([0-9]{,2}[dD][1-9][0-9]?)',rollString)
	if not baseroll:
		raise ValueError("Invalid roll string: %s"%(rollString))
	ammount,sides = re.split(r'[dD]',baseroll.group(1))
	if ammount == '': ammount = 1
	bonus = re.match(r'^.*[\+ p]([0-9]{1,5})', rollString)
	plus = bonus.group(1) if bonus else 0
	return ammount, sides, plus


class Roll(object):
	def __init__(self, sides=6, ammount=1, plus=0):
		self.sides=sides
		self.ammount=ammount
		self.plus=plus
		self.results=self.roll()

	@classmethod
	def from_string(cls, rollString):
		ammount, sides, plus = parseRoll(rollString)
		return cls(ammount,sides,plus)

	def roll(self):
		return [randint(1,self.sides) for i in range(self.ammount)]
		
	def total(self):
		return sum(self.results)+self.plus

	def __str__(self):
		return '['+','.join(map(str,self.results))+']'

	def __int__(self):
		return sum(self.results)+self.plus