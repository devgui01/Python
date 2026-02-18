#Game1
"""
Rock Paper Scissors :
"R" = "Rock"
"P" = "Paper"
"S" = "Scissor"
"""
import random
def play_game(user_choice):
    computer_choice = random.choice(["R","P","S"])
    choices_dict = {"R":"Rock","P":"Paper","S":"Scissor"}
    print(f"You Choose {choices_dict.get(user_choice)} and Computer Choose {choices_dict.get(computer_choice)}")
    if(user_choice == computer_choice):
        game_result = "Draw"
    else:
        if(user_choice == "R" and computer_choice == "P"):
            game_result = "You Lose, Try Again"
        elif(user_choice == "R" and computer_choice == "S"):
            game_result = "You Won"
        elif(user_choice == "S" and computer_choice == "R"):
            game_result = "You Lose, Try Again"
        elif(user_choice == "S" and computer_choice == "P"):
            game_result = "You Won"
        elif(user_choice == "P" and computer_choice == "S"):
            game_result = "You Lose, Try Again"
        elif(user_choice == "P" and computer_choice == "R"):
            game_result = "You Won"
        else:
            game_result = "Something Wents Wrong"
    return game_result


print(play_game(user_choice = input(f"R - Rock\nP - Paper\nS - Scissor\nChoose Any of these : ").upper()))
