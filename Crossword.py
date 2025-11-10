def can_place_horizontally(board, word, row, col):
    if col + len(word) > len(board[0]):
        return False
    if col > 0 and board[row][col - 1] != '+':
        return False
    if col + len(word) < len(board[0]) and board[row][col + len(word)] != '+':
        return False
    for i in range(len(word)):
        if board[row][col + i] not in ('-', word[i]):
            return False
    return True

def can_place_vertically(board, word, row, col):
    if row + len(word) > len(board):
        return False
    if row > 0 and board[row - 1][col] != '+':
        return False
    if row + len(word) < len(board) and board[row + len(word)][col] != '+':
        return False
    for i in range(len(word)):
        if board[row + i][col] not in ('-', word[i]):
            return False
    return True

def place_horizontally(board, word, row, col):
    positions = []
    for i in range(len(word)):
        if board[row][col + i] == '-':
            board[row][col + i] = word[i]
            positions.append((row, col + i))
    return positions

def place_vertically(board, word, row, col):
    positions = []
    for i in range(len(word)):
        if board[row + i][col] == '-':
            board[row + i][col] = word[i]
            positions.append((row + i, col))
    return positions

def remove_word(board, positions):
    for x, y in positions:
        board[x][y] = '-'

def solve_crossword(board, words, index):
    if index == len(words):
        for row in board:
            print(''.join(row))
        print()
        return True
    word = words[index]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if can_place_horizontally(board, word, i, j):
                placed = place_horizontally(board, word, i, j)
                if solve_crossword(board, words, index + 1):
                    return True
                remove_word(board, placed)
            if can_place_vertically(board, word, i, j):
                placed = place_vertically(board, word, i, j)
                if solve_crossword(board, words, index + 1):
                    return True
                remove_word(board, placed)
    return False

board = [
    ['+', '-', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '-', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '-', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '-', '-', '-', '-', '-', '+', '+', '+', '+'],
    ['+', '-', '+', '+', '+', '-', '+', '+', '+', '+'],
    ['+', '-', '+', '+', '+', '-', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '-', '+', '+', '+', '+'],
    ['+', '+', '-', '-', '-', '-', '-', '-', '+', '+'],
    ['+', '+', '+', '+', '+', '-', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '-', '+', '+', '+', '+']
]

words = ["DELHI", "ICELAND", "ANKARA", "LONDON"]

print("🔹 Crossword Puzzle Filler:\n")
if not solve_crossword(board, words, 0):
    print("No valid arrangement found.")
