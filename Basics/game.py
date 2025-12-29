#Game1
"""
Rock Paper Scissors :
"R" = "Rock"
"P" = "Paper"
"S" = "Scissor"
"""
import random
def Game(userinput):
    comp = random.choice(["R","P","S"])
    d1 ={"R":"Rock","P":"Paper","S":"Scissor"}
    print(f"You Choose {d1.get(userinput)} and Computer Choose {d1.get(comp)}")
    if(userinput==comp):
        output = "Draw"
    else:
        if(userinput == "R" and comp == "P"):
            output = "You Lose, Try Again"
        elif(userinput == "R" and comp == "S"):
            output = "You Won"
        elif(userinput == "S" and comp == "R"):
            output = "You Lose, Try Again"
        elif(userinput == "S" and comp == "P"):
            output = "You Won"
        elif(userinput == "P" and comp == "S"):
            output = "You Lose, Try Again"
        elif(userinput == "P" and comp == "R"):
            output = "You Won"
        else:
            output = "Something Wents Wrong"
    return output


print(Game(userinput = input(f"R - Rock\nP - Paper\nS - Scissor\nChoose Any of these : ").upper()))

