import re
from random import randint

def parseString(rollString):
	breakdown={}

	# Regex to grab anything that looks like a standard die roll
	# e.g. 1d6, d20, 2d8, up to 99d99
	baseroll = re.match(r'([0-9]{,2}[dD][1-9][0-9]?)',rollString)
	if not baseroll:
		raise ValueError("Invalid roll string: %s"%(rollString))
	ammount,sides = re.split(r'[dD]',baseroll.group(1))
	breakdown['sides']=int(sides)
	breakdown['ammount'] = int(ammount) if ammount else 1

	# Grabbing what looks like a bonus 
	bonus = re.match(r'^.*[\+ p]([0-9]{1,5})', rollString)
	breakdown['bonus'] = int(bonus.group(1)) if bonus else 0

	# Grabbing keep, to drop the lowest n rolls.
	# e.g. 4d6k3, 4d6^3
	keep = re.match(r'^.*[\^p]([0-9{0,2}])',rollString)
	if keep: 
		breakdown['keep'] = keep.group(1) if keep.group(1) < breakdown['ammount'] else breakdown['ammount']-1
	
	# Grabbing drop, to drop the highest n rolls.
	drop = re.match(r'^.*[vd]([0-9{0,2}])',rollString)
	if drop: 
		breakdown['drop'] = drop.group(1) if drop.group(1) < breakdown['ammount'] else breakdown['ammount']-1

	return breakdown


class Roll(object):
	def __init__(self, sides=6, ammount=1, bonus=0):
		self.ammount = ammount if ammount > 0 else 1
		self.sides = sides if sides > 0 else 1
		self.bonus = bonus
		self.results=self.roll()

	@classmethod
	def from_string(cls, rollString):
		ps = parseString(rollString)
		return cls(ps['sides'],ps['ammount'],ps['bonus'])

	def roll(self):
		return [randint(1,self.sides) for i in range(self.ammount)]
		
	def total(self):
		return sum(self.results)+self.bonus

	def __str__(self):
		return '['+','.join(map(str,self.results))+']'

	def __int__(self):
		return sum(self.results)+self.bonus