import random

OPTIONS = ["R", "S", "P"]  # store the value for rock, paper and scissors


def user_input():
    """takes in no argument and returns  either 'R', 'P' or 'S' from the user input.
     """
    # collect user input
    user_entry = input("Please Enter 'R' for Rock, 'P' for Paper "
                       "and 'S' for Scissors\n").upper()

    # check if user input is valid. Becomes recursive, if user input isn't valid
    if user_entry not in OPTIONS:
        print("please enter a valid input")
        user_entry = user_input()
    return user_entry


def computer_entry():
    """takes in no argument and returns either 'R', 'P' or 'S'
    after selecting at random"""

    comp_entry = random.choice(OPTIONS)
    return comp_entry


def compare(user_ent, comp_ent):
    """takes in two arguments returns a win, lose or
    draw after comparing it with the winning combo"""

    combo_dict = {"R": "Rock",
                  "P": "Paper",
                  "S": "Scissors"}

    print(f"Player ({combo_dict[user_ent]}) : "
          f"CPU ({combo_dict[comp_ent]})")

    combo = [user_ent, comp_ent]
    winning_combo = [["R", "S"], ["S", "P"], ["P", "R"]]

    if user_ent == comp_ent:
        return "draw"
    elif combo in winning_combo:
        return "win"

    return "lose"


def game_play():
    a = user_input()
    b = computer_entry()
    c = compare(user_ent=a, comp_ent=b)
    return c


result = game_play()
game_on = True
while game_on:
    if result == "draw":
        result = game_play()
    else:
        print(f"you {result}")
        game_on = False
