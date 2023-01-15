import unittest
import getopt
import sys
from src.word_search.solver import word_search_solver

class TestWordSearchSolver(unittest.TestCase):

	def test_word_search_solver(self):
		self.assertEqual(word_search_solver(), 0)

if __name__ == "__main__":
	verbose = False
	words = ""
	puzzle_grid = []

	# Process/parse arguments
	arg_list = []
	if len(sys.argv) > 1:
		arg_list = sys.argv[1:]
	options = "vi:l:"
	long_options = ["input_file=", "wordlist="]
	try:
		args, vals = getopt.getopt(arg_list, options, long_options)
		for currentArg, currentVal in args:
			if currentArg in ("-v", "--verbose"):
				verbose = True
			elif currentArg in ("-i", "--input_file"):
				f = open(str(currentVal), "r")
				for line in f:
					if line[-1] == "\n":
						puzzle_grid.append(line.split(" ")[:-1])
					else:
						puzzle_grid.append(line.split(" "))
				f.close()
			elif currentArg in ("-l", "--wordlist"):
				f = open(str(currentVal), "r")
				for line in f:
					if words == "":
						words += line
					else:
						words += " " + line
				f.close()
	# Error msgs for command line arguments
	except getopt.error as err:
		if err.opt in ("-i", "--input_file"):
			print("ERROR: Must provide an input file containing word search grid", file=sys.stderr)
		elif err.opt in ("-l", "--wordlist"):
			print("ERROR: Must provide wordlist for corresponding word search grid", file=sys.stderr)
		else:
			print("ERROR: Invalid argument", file=sys.stderr)
		sys.exit(-1)

	# Enforcing command line args
	if puzzle_grid == [] or words == "":
		print("ERROR: Must provide word search grid and/or word list", file=sys.stderr)
		sys.exit(-1)

	# Display word search grid
	if verbose:
		print("Displaying Word Search Grid")
		for y in puzzle_grid:
			for x in y:
				print(x + " ", end="")
			print("")
		print("")

	unittest.main()