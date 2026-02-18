"""
Game with High Score System

Play Rock-Paper-Scissors and beat your high score!
"""

import random


def play_game():
    """Play Rock-Paper-Scissors and return the score"""
    current_score = 0
    while True:
        choices = {"R": "Rock", "P": "Paper", "S": "Scissor"}
        user_input = input('"R" For Rock\n"P" For Paper\n"S" For Scissor\nEnter Your Choice: ').upper()
        computer_choice = random.choice(["R", "P", "S"])
        
        print(f"\nYou Choose {choices.get(user_input)} and Opponent Choose {choices.get(computer_choice)}")
        
        if user_input == computer_choice:
            game_result = "Draw"
        elif ((user_input == "R" and computer_choice == "S") or
              (user_input == "P" and computer_choice == "R") or
              (user_input == "S" and computer_choice == "P")):
            game_result = "You Win"
            current_score += 1
        else:
            game_result = "You Lose! Try Again"
            current_score = 0
        
        print(game_result)
        print(f"Score: {current_score}")
        
        retry_input = input('Press "R" for Retry: ').lower()
        if retry_input == "r":
            continue
        else:
            break
    
    return current_score


def update_high_score():
    """Read and update high score"""
    try:
        with open("Hi_Score.txt", "r") as score_file:
            file_data = score_file.read()
            previous_score = int(file_data) if file_data else 0
    except FileNotFoundError:
        previous_score = 0
    
    current_score = play_game()
    
    if current_score > previous_score:
        with open("Hi_Score.txt", "w") as score_file:
            score_file.write(str(current_score))
        print(f"New High Score: {current_score}")
    else:
        print(f"Score remains {previous_score}")


if __name__ == "__main__":
    update_high_score()
