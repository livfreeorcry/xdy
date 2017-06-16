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
		rv = self.app.get('/')

	def test_static_roll_get(self):
		rv1 = self.app.get('/?text=1d1+1')
		rv2 = self.app.get('/?text=1d1')
		rv3 = self.app.get('/?text=d6')
		rv4 = self.app.get('/?text=4d1k1')
		assert b'Rolled 1d1 1 and got: *2*' in rv1.data
		assert b' + 1' not in rv2.data
		assert b'd6' in rv3.data
		assert b'Dropped: [1, 1, 1]' in rv4.data

	def test_string_results(self):
		rv = str(dice.Roll(1))
		assert rv == "[1]"

	def test_int_results(self):
		rv = int(dice.Roll(1,5,1))
		assert rv == 6

	def test_regex_parser(self):
		rv = dice.parseString("5d6+1")
		assert 6 == rv['sides']
		assert 5 == rv['ammount']
		assert 1 == rv['bonus']
		

if __name__ == '__main__':
	unittest.main()