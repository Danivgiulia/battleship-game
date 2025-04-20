# Legend

# The 'X' mark will be used to mark a shot
# The ' ' (the empty space) will signify that nothing has been done
# The 'O' wil signify that the shot has been missed

# This will be used to generate random ship coorddinates
from random import randint

# The hidden board is for the computer to place the randomly generated
# coordinates
HIDDEN_BOARD = [[' '] * 8 for x in range(8)]

# The guess board is for the player to guess and keep track of where to put
# the shots
GUESS_BOARD = [[' '] * 8 for x in range(8)]

# Because python is a language that starts the count from 0 instead
# of 1, the letters to numbers have a range of 0-7
letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                      'E': 4, 'F': 5, 'G': 6, 'H': 7, }


# function for printing board
def print_battleship_board(board):
    print('')
    print('  A B C D E F G H')
    print('-----------------')
    row_number = 1
    for row_number, row in enumerate(board, start=1):
        print(f"{row_number}|{'|'.join(row)}|")


# function for creating the ships randomly
def generate_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'X'


# function for getting the ship location
# bug for if no input then crash
def get_coordinates():
    print()

    # Get valid row input
    while True:
        row = input('Please enter a ship row (1-8): ')
        if row in '12345678':
            break
        print('Please enter a valid row.')

    # Get valid column input
    while True:
        column = input('Please enter a ship column (A-H): ').upper()
        if column in 'ABCDEFGH':
            break
        print('Please enter a valid column.')

    return int(row) - 1, letters_to_numbers[column]


# function that counts the total hits
def total_hits(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


generate_ships(HIDDEN_BOARD)

turns = 10

print(
    "Welcome to Battleship!\n"
    "In Battleship, you will take turns guessing the row (1-8) and \n"
    "column (A-H) coordinates to locate and hit five hidden enemy ships \n"
    "on an 8x8 grid.\n"
    "You have 10 turns to sink all the ships before time runs out!\n"
)

while turns > 0:
    print_battleship_board(GUESS_BOARD)
    row, column = get_coordinates()

    # Check if the user already guessed that location
    if GUESS_BOARD[row][column] in ['O', 'X']:
        print('\nYou already guessed that spot. Try again.')
        continue  # Skip the rest of this loop and go to the next guess

    # Check for a hit
    if HIDDEN_BOARD[row][column] == 'X':
        print('\n Hit! You’ve struck a battleship!')
        GUESS_BOARD[row][column] = 'X'
    else:
        print('\n Miss!')
        GUESS_BOARD[row][column] = 'O'

    turns -= 1

    # Check for win condition
    if total_hits(GUESS_BOARD) == 5:
        print('\n Congratulations, you have sunk all the battleships!')
        break

    print(f'You have {turns} turn{"s" if turns != 1 else ""} remaining.\n')

    # Check for game over
    if turns == 0:
        print(' Sorry, you have run out of turns. The game is over.')
        break
