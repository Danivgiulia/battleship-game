HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
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
    for row_number, row in enumerate(board, start = 1):
        print(f"{row_number}|{'|'.join(row)}|")
print()

# function for creating the ships randomly
def generate_ships():
    pass

# function for getting the ship location
# bug for if no input then crash
def get_coordinates():
    pass

# function that counts the total hits
def total_hits():
    pass

print_battleship_board(HIDDEN_BOARD)
print_battleship_board(GUESS_BOARD)