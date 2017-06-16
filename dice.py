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
	bonus = re.match(r'^.*[\+ ]([0-9]{1,5})', rollString)
	breakdown['bonus'] = int(bonus.group(1)) if bonus else 0

	#Grabbing a penalty, if there's no bonus
	if not bonus: 
		penalty = re.match(r'^.*[\-]([0-9]{1,5})', rollString)
		if penalty: breakdown['bonus'] = int(penalty.group(1))*-1 

	# Grabbing keep, to drop the lowest n rolls.
	# e.g. 4d6k3, 4d6^3
	keep = re.match(r'^.*[\^k]([0-9{0,2}])',rollString)
	if keep: 
		breakdown['keep'] = int(keep.group(1))
	
	# Grabbing drop, to drop the highest n rolls.
	drop = re.match(r'^.*[v]([0-9{0,2}])',rollString)
	if drop: 
		breakdown['drop'] = int(drop.group(1))

	return breakdown


class Roll(object):
	def __init__(self, sides=6, ammount=1, bonus=0):
		self.ammount = ammount if ammount > 0 else 1
		self.sides = sides if sides > 0 else 1
		self.bonus = bonus
		self.results=self.roll()

	@classmethod
	def from_string(cls, rollString):
		# using a string like '4d6+5'
		ps = parseString(rollString)
		return cls(ps['sides'],ps['ammount'],ps['bonus'])

	def roll(self):
		self.results = [randint(1,self.sides) for i in range(self.ammount)]
		return self.results
		
	def total(self):
		return sum(self.results)+self.bonus

	def drop(self, keep):
		self.results.sort()
		keep = len(self.results)-keep
		return [self.results.pop(-1) for i in range(keep)]

	def keep(self, keep):
		self.results.sort()
		keep = len(self.results)-keep
		return [self.results.pop(0) for i in range(keep)]

	def __str__(self):
		return '['+','.join(map(str,self.results))+']'

	def __int__(self):
		return self.total()