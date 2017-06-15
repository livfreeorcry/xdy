import os
import slackroller
import dice
import unittest
import tempfile

class SlackrollerTestCase(unittest.TestCase):

	def setUp(self):
		slackroller.app.testing = True
		self.app = slackroller.app.test_client()

	def tearDown(self):
		pass

	def test_response(self):
		print '\nblank response test'
		rv = self.app.get('/')

	def test_static_roll_get(self):
		print '\nTests through flask...'
		rv1 = self.app.get('/?text=1d1+1')
		rv2 = self.app.get('/?text=1d1')
		assert b'Rolled 1d1 1 and got: *2*' in rv1.data
		assert b' + 1' not in rv2.data
		print 'flask tests finished'

	def test_string_results(self):
		print '\n__str__ method'
		rv = str(dice.Roll(1,1,1))
		assert rv == "[1]"

	def test_int_results(self):
		print '\n__int__ method'
		rv = int(dice.Roll(1,5,1))
		assert rv == 6

	def test_parser(self):
		print '\nold parser'
		rv = dice.parseRoll("1d1+1")

	def test_regex_parser(self):
		print '\nregex parser'
		rv = dice.parseString("5d6+1")
		print rv
		assert ('5','6','1') == rv



if __name__ == '__main__':
	unittest.main()