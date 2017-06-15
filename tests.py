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
		rv = self.app.get('/?text=1d1+1')
		assert b'Rolled 1d1 1 and got: *2*' in rv.data

	def test_string_results(self):
		rv = str(dice.Roll(1,1,1))
		assert rv == "[1]"

	def test_int_results(self):
		rv = int(dice.Roll(1,5,1))
		assert rv == 6

if __name__ == '__main__':
	unittest.main()