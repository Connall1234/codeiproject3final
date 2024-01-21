import random
# Player's global lists for misses, hits, and boats
miss_ship_player = []
hit_ship_player = []
boat_player = []

# Computer's global lists for misses, hits, and boats
miss_ship_computer = []
hit_ship_computer = []
boat_computer = []

"""List to track the computer's guesses"""
computer_poss_guesses = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]


class Board:
    """
    Class to create and manage the game board.
    """
    def __init__(self, board_size, whos_playing, type):
        self.board_size = board_size
        self.whos_playing = whos_playing
        self.type = type

    """Function to print the game boards with misses, hits, and ships."""
    def print_board(self, miss_ship, hit_ship, boat):
        place = 0
        print("__________________")
        print(f"\n{self.whos_playing}'s board\n")
        print("__________________")
        print("     0  1  2  3  4")
        for point in range(5):
            row = ""
            for y in range(5):
                ch = " _ "
                if place in miss_ship:
                    ch = " x "
                elif place in hit_ship:
                    ch = " o "
                elif self.type == "Type A" and place in boat:
                    ch = " @ "
                row = row + ch
                place = place + 1
            print(point, " ", row)


def get_player_name():
    """Function to get the player's name with user input validation."""
    trigger = "off"
    while trigger == "off":
        try:
            name_not_capitalized = input("What is your name, please use three letters only. ")
            if len(name_not_capitalized) != 3 or not name_not_capitalized.isalpha():
                raise ValueError("Wrong amount of characters or invalid input, try again! ")
            name = name_not_capitalized.capitalize()
            return name
            trigger = "on"
        except ValueError as e:
            print("Error:", e)


def print_boats(boat):
    """Function to randomly assign ships to the board."""
    random_numbers = random.sample(range(0, 24), 6)
    boat.extend(random_numbers)
    return boat


def get_hit(hit_ship_player, miss_ship_player, boat_player):
    """Function to get player's hit position with input validation."""
    while True:
        try:
            column_select = int(input("\nPlease select a column? "))
            if column_select in range(0, 5):
                break
            else:
                print("\nThat's off the board!")
        except ValueError as e:
            print("\nPssst, it's meant to be a number!")
    while True:
        try:
            row_select = int(input("\nPlease select a row? "))
            if row_select in range(0, 5):
                break
            else:
                print("\nThat's off the board!")
        except ValueError as e:
            print("\nHey now, it's meant to be a number!")
    return (column_select * 5) + row_select


def player_turn(hit_ship_player, miss_ship_player, boat_player):
    """Function for player's turn with input validation."""
    player_hit = None
    while True:
        player_hit = get_hit(hit_ship_player, miss_ship_player, boat_player)
        if player_hit in hit_ship_player or player_hit in miss_ship_player:
            print("Looks like you had that guess!")
        else:
            break
    return player_hit


def computer_guess(computer_poss_guesses):
    """Function to get computer's guess from the available list."""
    computer_hit = random.choice(computer_poss_guesses)
    computer_poss_guesses.remove(computer_hit)
    return computer_hit


def check(miss, hit, boat, result):
    """Function to check if the guess hit or miss."""
    if result in boat:
        boat.remove(result)
        hit.append(result)
    else:
        miss.append(result)


def check_comp(miss, hit, boat, result):
    """Function to check computer's guess and update lists accordingly."""
    if result in boat:
        boat.remove(result)
        hit.append(result)
    else:
        miss.append(result)
