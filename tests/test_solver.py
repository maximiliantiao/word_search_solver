from word_search_solver.solver import word_search_solver
import unittest
import getopt
import sys

class TestWordSearchSolver(unittest.TestCase):

	def test_word_search_solver(self):
		self.assertEqual(word_search_solver(), 0)


if __name__ == "__main__":
	unittest.main()