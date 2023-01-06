import sys
import getopt
import subprocess
import time

def r_search(grid, word, index, x, y, dir, reverse=False):
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
            if reverse:
                index -= 1
            else:
                index += 1
            # Search N direction
            if dir == "N" and r_search(grid, word, index, x, y - 1, "N", reverse) == 1:
                return 1
            # Search NE direction
            elif dir == "NE" and r_search(grid, word, index, x + 1, y - 1, "NE", reverse) == 1:
                return 1
            # Search E direction
            elif dir == "E" and r_search(grid, word, index, x + 1, y, "E", reverse) == 1:
                return 1
            # Search SE direction
            elif dir == "SE" and r_search(grid, word, index, x + 1, y + 1, "SE", reverse) == 1:
                return 1
            # Search S direction
            elif dir == "S" and r_search(grid, word, index, x, y + 1, "S", reverse) == 1:
                return 1
            # Search SW direction
            elif dir == "SW" and r_search(grid, word, index, x - 1, y + 1, "SW", reverse) == 1:
                return 1
            # Search W direction
            elif dir == "W" and r_search(grid, word, index, x - 1, y, "W", reverse) == 1:
                return 1
            # Search NW direction
            elif dir == "NW" and r_search(grid, word, index, x - 1, y - 1, "NW", reverse) == 1:
                return 1
            else:
                return 0
        # If current character is not found
        else:
            return 0

def base_search(grid, word, reverse=False):
    # Iterate through each row of word search grid
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if reverse:
                starting_index = len(word) - 1
            else:
                starting_index = 0
            # Find letter
            if grid[y][x] == word[starting_index]:
                # Begin search
                status_code = r_search(grid, word, starting_index, x, y, "N", reverse) + r_search(grid, word, starting_index, x, y, "NE", reverse) \
                            + r_search(grid, word, starting_index, x, y, "E", reverse) + r_search(grid, word, starting_index, x, y, "SE", reverse) \
                            + r_search(grid, word, starting_index, x, y, "S", reverse) + r_search(grid, word, starting_index, x, y, "SW", reverse) \
                            + r_search(grid, word, starting_index, x, y, "W", reverse) + r_search(grid, word, starting_index, x, y, "NW", reverse)
                # if status_code == 1:
                #     print("%s found at (%d, %d)" % (word, x, y))

if __name__ == "__main__":
    '''
    Word Search #146 + 5 words = 40 words
    '''
    # Word List
    words = "action adrift airplane approach arboretum blacktop bridesmaid burrow cardinal caviar coffee dangle engineer eyetooth \
            foothold heliport herdsman interactive lawman needless pinwheel pliers porter praise recent relation resistance retain  \
            saucer senior serenade streamline toddle treaty triangle underway whiten vicarious xylophone zealous"
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
    # for y in puzzle_grid:
    #     for x in y:
    #         print(x + " ", end="")
    #     print("")
    
    # Solve word search starting from first letter of words and time for performance
    print("Searching words from first letter")
    avg_time = 0
    fastest_time = 10000000000000000
    slowest_time = 0
    for i in range(1000):
        start = time.perf_counter()
        for word in words.split():
            base_search(puzzle_grid, word.upper())
        end = time.perf_counter()
        avg_time += 1000 * (end - start)
        fastest_time = min(fastest_time, 1000 * (end - start))
        slowest_time = max(slowest_time, 1000 * (end - start))

    print(f"Average solve time: {(avg_time / 1000):0.4f} ms")
    print(f"Solve time (fastest/slowest): {fastest_time:0.4f} / {slowest_time:0.4f} ms")

    print("")

    # Solve word search starting from last letter of words and time for performance
    print("Searching words from last letter")
    avg_time = 0
    fastest_time = 10000000000000000
    slowest_time = 0
    for i in range(1000):
        start = time.perf_counter()
        for word in words.split():
            base_search(puzzle_grid, word.upper(), reverse=True)
        end = time.perf_counter()
        avg_time += 1000 * (end - start)
        fastest_time = min(fastest_time, 1000 * (end - start))
        slowest_time = max(slowest_time, 1000 * (end - start))

    print(f"Average solve time: {(avg_time / 1000):0.4f} ms")
    print(f"Solve time (fastest/slowest): {fastest_time:0.4f} / {slowest_time:0.4f} ms")
    

