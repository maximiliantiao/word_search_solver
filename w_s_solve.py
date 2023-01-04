import sys
import getopt
import subprocess

def r_search(grid, word, index, x, y):
    if (index == len(word)):
        return 1
    elif ((x < 0) or (y < 0) or (x == len(grid[0])) or (y == len(grid))):
        return 0
    else:
        if grid[y][x] == word[index]:
            index += 1
            # Search N
            return (r_search(grid, word, index, x, y - 1) | r_search(grid, word, index, x + 1, y - 1) \
                |  r_search(grid, word, index, x + 1, y) | r_search(grid, word, index, x + 1, y + 1) \
                |  r_search(grid, word, index, x, y + 1) | r_search(grid, word, index, x - 1, y + 1) \
                |  r_search(grid, word, index, x - 1, y) | r_search(grid, word, index, x - 1, y - 1)) \
                *  (index == len(word))
        return 0

def base_search(grid, word):
    # Iterate through each row of grid
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            # Find first letter
            if grid[y][x] == word[0].capitalize():
                r_search(grid, word, 0, x, y)
                print("%s found at (%d, %d)" % (word, x, y))


if __name__ == "__main__":
    
    '''
    arg_list = []
    if len(sys.argv) > 1:
        arg_list = sys.argv[1:]

    options = "s:d:w:r"

    long_options = ["size=", "difficulty=", "words=", "random_words"]

    try:
        args, vals = getopt.getopt(arg_list, options, long_options)
        for currentArg, currentVal in args:
            if currentArg in ("-s", "--size"):
                print("Puzzle size: %s" % (str(currentVal)))
            elif currentArg in ("-d", "--difficulty"):
                print("Difficulty Level: %s" % (str(currentVal)))
            elif currentArg in ("-w", "--words"):
                print("Words: ", currentVal.split(","))
            elif currentArg in ("-r", "--random_words"):
                print("Use random words")

    except getopt.error as err:
        if err.opt in ("s", "size"):
            print("ERROR: 5 <= size <= 50", file=sys.stderr)
        elif err.opt in ("d", "difficulty"):
            print("ERROR: 1 <= difficulty <= 7", file=sys.stderr)
        elif err.opt in ("w", "words"):
            print("ERROR: Words need to be listed", file=sys.stderr)
        sys.exit(-1)
    '''

    words = "dog cat pig"
    word_search_command = "word-search" + " " + words
    word_search_process = subprocess.Popen(word_search_command.split(), stdout=subprocess.PIPE)
    output, error = word_search_process.communicate()
    raw_puzzle = output.decode().split('\n')[3:-6]
    puzzle_grid = []
    for row in raw_puzzle:
        puzzle_grid.append(row.split(" "))
        print(puzzle_grid[-1])

    for word in words.split():
        print("Finding %s" % (word))
        base_search(puzzle_grid, word)

    

