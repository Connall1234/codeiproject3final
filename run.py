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


def check_winner(boat_player, boat_computer):
    """Function to check for the winner or draw."""
    if len(boat_computer) == 0 and len(boat_player) == 0:
        print("\nAll ships are down, it's a tie! ")

        return True
    elif len(boat_computer) == 0:
        print("\nComputer ships are down, you win! ")
        return True
    elif len(boat_player) == 0:
        print("\nYour ships are down, computer wins! ")
        return True
    else:
        return


def print_hits(result, miss, hit, player):
    """Function to print information about the hits and misses."""
    if result in hit:
        print(f"\n{player} guessed {result}, it was a hit!")
    elif result in miss:
        print(f"\n{player} guessed {result}, it was a miss")


def print_instruction():
    """Function to print game instructions at the start."""
    print("\nWelcome to the Battleship Game!")
    print("You will play against the computer. Here are the rules:")
    print("1. You and the computer each have a fleet of ships, six each!.")
    print("2. Your goal is to sink all of the computer's ships before yours are sunk.")
    print("3. The game is played on a 5x5 board.")
    print("4. Ships are represented by '@'. Misses are marked with 'x', and hits are marked with 'o'.")
    print("The coordinates start from 0 and go up to 4, so make sure you stay within these numbers!")
    print("The coordinates range from 0-24 which, for another way to know where you're aiming. ")
    print("5. You and the computer will take turns guessing the coordinates to attack.")
    print("6. Enter row and column numbers when prompted to make a guess.")
    print("7. The game ends when either all your ships or the computer's ships are sunk, or a draw!.")
    print("8. You have 10 turns to defeat the computer. Use them wisely!")
    print("\nNow we've got that out of the way, ships ahoy!\n")


def main():
    """Main function to run the game."""
    global miss_ship_player, hit_ship_player, boat_player, miss_ship_computer, hit_ship_computer, boat_computer, computer_poss_guesses
    print_instruction()
    turns = 10
    player_name = get_player_name()
    game_board = Board(5, "Computer", "Type A")
    player_print_boats = print_boats(boat_computer)
    game_board.print_board(miss_ship_player, hit_ship_player, boat_player)
    comp = Board(5, player_name, "Type B")
    computer_print_boats = print_boats(boat_player)
    comp.print_board(miss_ship_computer, hit_ship_computer, boat_computer)
    """Using for loop to give game turns"""
    for x in range(0, 10):
        turns -= 1
        result = player_turn(miss_ship_computer, hit_ship_computer, boat_computer)
        result_computer = computer_guess(computer_poss_guesses)
        check(miss_ship_computer, hit_ship_computer, boat_computer, result)
        check_comp(miss_ship_player, hit_ship_player, boat_player, result_computer)
        game_board.print_board(miss_ship_player, hit_ship_player, boat_player)
        comp.print_board(miss_ship_computer, hit_ship_computer, boat_computer)
        print(f"\nTurns: {turns}")
        print_hits(result, miss_ship_computer, hit_ship_computer, player_name)
        print_hits(result_computer, miss_ship_player, hit_ship_player, "Computer")
        """Using if statement to check winner"""
        if check_winner(boat_player, boat_computer):
            """While loop for input validation"""
            while True:
                try:
                    """Option to play again"""
                    play_again = input("\nThat's the game! Would you like to play again?\nHit y to play again, or n to quit! ")
                    if play_again == "y":
                        miss_ship_player = []
                        hit_ship_player = []
                        boat_player = []
                        miss_ship_computer = []
                        hit_ship_computer = []
                        boat_computer = []
                        computer_poss_guesses = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
                        main()
                    elif play_again == "n":
                        print("Goodbye! ")
                        return False
                except ValueError:
                    print("Please enter a valid choice! ")
        """If game ends in draw"""
        if turns == 0:
            while True:
                try:
                    play_again = input("\nThat's the game, shame it ended in a draw, why don't you play again!\nHit y to play again, or n to quit! ")
                    if play_again == "y":
                        miss_ship_player = []
                        hit_ship_player = []
                        boat_player = []
                        miss_ship_computer = []
                        hit_ship_computer = []
                        boat_computer = []
                        computer_poss_guesses = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
                        main()
                    elif play_again == "n":
                        print("Goodbye! ")
                        return False
                except ValueError:
                    print("Please enter a valid choice! ")

main()