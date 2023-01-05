import sys
import getopt
import subprocess
import time

def r_search(grid, word, index, x, y, dir):
    # Word found
    if (index == len(word)):
        return 1
    # Searching beyond grid boundary
    elif ((x < 0) or (y < 0) or (x == len(grid[0])) or (y == len(grid))):
        return 0
    # Continue searching in current direction
    else:
        # If current character is found
        if grid[y][x] == word[index]:
            index += 1
            # Search N direction
            if dir == "N" and r_search(grid, word, index, x, y - 1, "N") == 1:
                return 1
            # Search NE direction
            elif dir == "NE" and r_search(grid, word, index, x + 1, y - 1, "NE") == 1:
                return 1
            # Search E direction
            elif dir == "E" and r_search(grid, word, index, x + 1, y, "E") == 1:
                return 1
            # Search SE direction
            elif dir == "SE" and r_search(grid, word, index, x + 1, y + 1, "SE") == 1:
                return 1
            # Search S direction
            elif dir == "S" and r_search(grid, word, index, x, y + 1, "S") == 1:
                return 1
            # Search SW direction
            elif dir == "SW" and r_search(grid, word, index, x - 1, y + 1, "SW") == 1:
                return 1
            # Search W direction
            elif dir == "W" and r_search(grid, word, index, x - 1, y, "W") == 1:
                return 1
            # Search NW direction
            elif dir == "NW" and r_search(grid, word, index, x - 1, y - 1, "NW") == 1:
                return 1
            else:
                return 0
        # If current character is not found
        else:
            return 0

def base_search(grid, word):
    # Iterate through each row of word search grid
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            # Find first letter
            if grid[y][x] == word[0]:
                # Begin search
                status_code = r_search(grid, word, 0, x, y, "N") + r_search(grid, word, 0, x, y, "NE") \
                            + r_search(grid, word, 0, x, y, "E") + r_search(grid, word, 0, x, y, "SE") \
                            + r_search(grid, word, 0, x, y, "S") + r_search(grid, word, 0, x, y, "SW") \
                            + r_search(grid, word, 0, x, y, "W") + r_search(grid, word, 0, x, y, "NW")
                if status_code == 1:
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
    '''
    Word Search #146
    '''
    # Word List
    words = "action adrift airplane approach blacktop bridesmaid burrow cardinal caviar coffee dangle engineer eyetooth \
            foothold heliport herdsman lawman needless pinwheel pliers porter praise recent relation resistance retain  \
            saucer senior serenade streamline toddle treaty triangle underway whiten"
    # Word Search Command
    word_search_command = "word-search -s 50 -d 7 " + words
    word_search_process = subprocess.Popen(word_search_command.split(), stdout=subprocess.PIPE)
    # Get output and error msgs
    output, error = word_search_process.communicate()
    # Splice out headers and footers
    raw_puzzle = output.decode().split('\n')[3:-6]
    puzzle_grid = []
    # Convert string to list of lists
    for row in raw_puzzle:
        puzzle_grid.append(row.split(" "))

    # Display word search grid
    for y in puzzle_grid:
        for x in y:
            print(x + " ", end="")
        print("")
    
    # Solve word search and time for performance
    start = time.perf_counter()
    for word in words.split():
        base_search(puzzle_grid, word.upper())
    end = time.perf_counter()
    print(f"Solved word search in {1000 * (end - start):0.4f} milliseconds")

    

