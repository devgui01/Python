"""
1.The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘score.txt’ which is either blank or
contains the previous score.You need to write a program to update the score whenever the game() function breaks the score.
"""

import random


def game():
    score = 0
    while True:
        l1 = {"R":"Rock","P":"Paper","S":"Scissor"}
        userin = input(f"\"R\" For Rock\n\"P\" For Paper\n\"S\" For Scissor\nEnter Your Choice : ").upper()
        comp = random.choice(["R","P","S"])
        print(f"\nYou Choose {l1.get(userin)} and Opponent Choose {l1.get(comp)}")
        if(userin==comp):
            WOL = "Draw"
        elif((userin=="R" and comp=="S") or (userin=="P" and comp=="R") or (userin=="S" and comp=="P")):
            WOL = "You Win"
            score+=1
        else:
            WOL = "You Lose ! Try Again"
            score=0
        print(WOL)
        print(f"Score: {score}")
        bol = input("Press \"R\" for Retry : ").lower()
        if(bol=="r"):
            continue
        else:
            break
    return score



def scoreupdate():
    with open("/Users/dartstorm/Desktop/Github/Python/Basics/Hi_Score.txt","r") as f:
                    data = f.read()
                    if(data == ""):
                        ps = 0
                        cs = game()
                        if(cs>ps):
                            with open("/Users/dartstorm/Desktop/Github/Python/Basics/Hi_Score.txt","w") as f:
                                f.write(str(cs))
                                print(f"New High Score {cs}")
                        else:
                            with open("/Users/dartstorm/Desktop/Github/Python/Basics/Hi_Score.txt","w") as f:
                                f.write(str(ps))
                                print(f"Score remains {ps}") 
                    else:
                        with open("/Users/dartstorm/Desktop/Github/Python/Basics/Hi_Score.txt","r") as f:
                            ps = f.read()
                            cs = game()
                            ps = int(ps)
                            if(cs>ps):
                                with open("/Users/dartstorm/Desktop/Github/Python/Basics/Hi_Score.txt","w") as f:
                                    f.write(str(cs))
                                    print(f"New High Score {cs}")
                            else:
                                with open("/Users/dartstorm/Desktop/Github/Python/Basics/Hi_Score.txt","w") as f:
                                    f.write(str(ps))
                                    print(f"Score remains {ps}") 

                               
scoreupdate()


        




