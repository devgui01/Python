#Game1
"""
Rock Paper Scissors :
"R" = "Rock"
"P" = "Paper"
"S" = "Scissor"
"""
import random
def Game(userinput):
    computer_choice = random.choice(["R","P","S"])
    choices_dict = {"R":"Rock","P":"Paper","S":"Scissor"}
    print(f"You Choose {choices_dict.get(userinput)} and Computer Choose {choices_dict.get(computer_choice)}")
    if(userinput==computer_choice):
        output = "Draw"
    else:
        if(userinput == "R" and computer_choice == "P"):
            output = "You Lose, Try Again"
        elif(userinput == "R" and computer_choice == "S"):
            output = "You Won"
        elif(userinput == "S" and computer_choice == "R"):
            output = "You Lose, Try Again"
        elif(userinput == "S" and computer_choice == "P"):
            output = "You Won"
        elif(userinput == "P" and computer_choice == "S"):
            output = "You Lose, Try Again"
        elif(userinput == "P" and computer_choice == "R"):
            output = "You Won"
        else:
            output = "Something Wents Wrong"
    return output


print(Game(userinput = input(f"R - Rock\nP - Paper\nS - Scissor\nChoose Any of these : ").upper()))

