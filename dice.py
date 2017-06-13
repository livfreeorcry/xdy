import re
from random import randint

class Roll(object):
	def __init__(self, rollString):
		self.rollString=rollString
		self.numDice, self.die, self.plus = self.parseRoll(rollString)


	def throw(self):
		# self.result=randint(1,self.die)
		result=[]
		for i in range(self.numDice):
			result.append(randint(1,self.die))
		return result

	def parseRoll(self, rollString):
		numDice = 1
		plus = 0
		regex = r'^[0-9]{,2}[dD][1-9][0-9]?(\+[0-9]{1,5})?$'
		if not re.match(regex,rollString):
			raise ValueError('Invalid roll string: %s' %(rollString))
		splitString = re.split(r'[d\+]+',rollString)
		if len(splitString)==3 and splitString[0] != '':
			numDice, die, plus = splitString
		elif len(splitString)==3 and splitString[0] == '':
			blank, die, plus = splitString
		elif len(splitString)==2 and splitString[0] != '':
			numDice, die = splitString
		else:
			die=splitString[1]
		return [int(numDice), int(die), int(plus)]
		# return [1,2,3]
		
	def roll(self):
		throw = self.throw()
		return sum(throw)+self.plus