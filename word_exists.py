'''
Given a 2D board of characters and a word, find if the word exists in the grid.

The word is considered to exist in the grid by starting anywhere on the grid and moving adjacent horizontally or vertically.
Each character can only be used one time.

EXAMPLE(S)
On this grid:  
[['A', 'B', 'C'],  
 ['D', 'E', 'F'],  
 ['G', 'H', 'I']]  

The word "ABEHI" exists.  
The word "AE" does not exist.  
The word "AC" does not exist. 
 
 "ABA" does not exist
'''

def word_exists(grid, word):
    def helper(row, col, i):
        if i == len(word):
            return True
        elif not 0 <= row < len(grid) or not 0 <= col < len(grid[0]) or (row, col) in visited:
            return False
        elif word[i] == grid[row][col]:
            visited.add((row, col))
            i += 1
            word_found = helper(row + 1, col, i) or helper(row - 1, col, i) or helper(row, col + 1, i) or helper(row, col - 1, i)
            visited.remove((row, col))
            return word_found
        return False

    visited = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if helper(row, col, 0):
                return True
    return False


grid = [['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I']]

grid2 = [['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I'],
        ['A', 'B', 'C']]

print(word_exists(grid, 'ABEHI') == True)
print(word_exists(grid, 'AE') == False)
print(word_exists(grid, 'AC') == False)
print(word_exists(grid, 'ABCB') == False)
print(word_exists(grid, 'ADGHIFCBE') == True)
print(word_exists(grid, 'ADGHIFCBEH') == False)
print(word_exists(grid, 'ABEHGD') == True)

print(word_exists(grid2, 'ABCIFCBA') == True)

print(word_exists([], 'A') == False)
print(word_exists([[]], '') == False)
