HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
GUESS_BOARD = [[' '] * 8 for x in range(8)]

# Because python is a language that starts the count from 0 instead
# of 1, the letters to numbers have a range of 0-7
letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                      'E': 4, 'F': 5, 'G': 6, 'H': 7, }

# function for printing board
def print_battleship_board():
    pass

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
