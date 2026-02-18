import random


def game():
    random_number = random.randint(1, 100)
    user_input = -1
    guess = 1
    while user_input != random_number:
        user_input = int(input(f"Guess the Number: "))
        if user_input > random_number:
            print("\t\tChoose a Lower number")
            guess += 1
        elif user_input < random_number:
            print("\t\tChoose a Higher number")
            guess += 1
        else:
            break
    return guess


def Multiplayer():
    guess = {}
    for i in range(2):
        guessed_val = game()
        print(f"Player {i+1} Guessed in {guessed_val} attempt\n")
        guess[f"Player {i}"] = guessed_val
    
    if guess["Player 0"] == guess["Player 1"]:
        print("Match Draw")
    elif guess["Player 0"] > guess["Player 1"]:
        print("Player 2 Won")
    elif guess["Player 0"] < guess["Player 1"]:
        print("Player 1 Won")
    else:
        print("Something Wrong Happen!")


Multiplayer()
