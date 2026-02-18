"""
Game with High Score System

Play Rock-Paper-Scissors and beat your high score!
"""

import random


def game():
    """Play Rock-Paper-Scissors and return the score"""
    score = 0
    while True:
        choices = {"R": "Rock", "P": "Paper", "S": "Scissor"}
        user_input = input('"R" For Rock\n"P" For Paper\n"S" For Scissor\nEnter Your Choice: ').upper()
        comp_choice = random.choice(["R", "P", "S"])
        
        print(f"\nYou Choose {choices.get(user_input)} and Opponent Choose {choices.get(comp_choice)}")
        
        if user_input == comp_choice:
            result = "Draw"
        elif ((user_input == "R" and comp_choice == "S") or
              (user_input == "P" and comp_choice == "R") or
              (user_input == "S" and comp_choice == "P")):
            result = "You Win"
            score += 1
        else:
            result = "You Lose! Try Again"
            score = 0
        
        print(result)
        print(f"Score: {score}")
        
        retry = input('Press "R" for Retry: ').lower()
        if retry != "r":
            break
    
    return score


def update_score():
    """Read and update high score"""
    try:
        with open("Hi_Score.txt", "r") as f:
            data = f.read()
            previous_score = int(data) if data else 0
    except FileNotFoundError:
        previous_score = 0
    
    current_score = game()
    
    if current_score > previous_score:
        with open("Hi_Score.txt", "w") as f:
            f.write(str(current_score))
        print(f"New High Score: {current_score}")
    else:
        print(f"Score remains {previous_score}")


if __name__ == "__main__":
    update_score()
