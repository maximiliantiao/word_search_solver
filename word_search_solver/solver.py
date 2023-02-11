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
        # Iterate through each column of word search grid
        for x in range(len(grid[y])):
            # Locate first letter of words
            if grid[y][x] == word[0]:
                # Begin search and display (x,y) coordinate and direction of word found
                if r_search(grid, word, 0, x, y, "N") == 1:
                    print("%s found at (%d, %d) N" % (word, x + 1, y + 1))
                elif r_search(grid, word, 0, x, y, "NE") == 1:
                    print("%s found at (%d, %d) NE" % (word, x + 1, y + 1))
                elif r_search(grid, word, 0, x, y, "E") == 1:
                    print("%s found at (%d, %d) E" % (word, x + 1, y + 1))
                elif r_search(grid, word, 0, x, y, "SE") == 1:
                    print("%s found at (%d, %d) SE" % (word, x + 1, y + 1))
                elif r_search(grid, word, 0, x, y, "S") == 1:
                    print("%s found at (%d, %d) S" % (word, x + 1, y + 1))
                elif r_search(grid, word, 0, x, y, "SW") == 1:
                    print("%s found at (%d, %d) SW" % (word, x + 1, y + 1))
                elif r_search(grid, word, 0, x, y, "W") == 1:
                    print("%s found at (%d, %d) W" % (word, x + 1, y + 1))
                elif r_search(grid, word, 0, x, y, "NW") == 1:
                    print("%s found at (%d, %d) NW" % (word, x + 1, y + 1))

def word_search_solver(input_file, wordlist, timing=False, verbose=False):
    words = []
    puzzle_grid = []

    # Open and read word search grid from provided input file
    try:
        f = open(input_file, "r")
        for line in f:
            line_split = line.split(" ")
            # Check for newline character attached to final character of each row of grid
            if '\n' in line_split[-1]:
                pop_elem = line_split.pop()
                line_split.append(pop_elem[0])
            puzzle_grid.append(line_split)
        f.close()
    except:
        print("ERROR: Must provide an input file containing word search grid", file=sys.stderr)
        return -1

    # Open and read word search wordlist from provided wordlist file
    try:
        f = open(wordlist, "r")
        for line in f:
            # Remove newline char in word
            cleaned_line = line.replace("\n", "")
            # Remove possible spaces in words that have multiple words
            cleaned_line = cleaned_line.replace(" ", "")
            words.append(cleaned_line)
        f.close()
    except:
        print("ERROR: Must provide wordlist for corresponding word search grid", file=sys.stderr)
        return -1

    # Display word search grid
    if verbose:
        print("Displaying Word Search Grid")
        for y in puzzle_grid:
            for x in y:
                print(x + " ", end="")
            print("")
        print("")

    # Solve word search and display answers and solve time
    print("Location of words are in (col, row) format")
    start = time.perf_counter()
    for word in words:
        base_search(puzzle_grid, word.upper())
    end = time.perf_counter()
    if timing:
        print(f"Solve time: {1000 * (end - start)} ms")

    return 0