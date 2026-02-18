# Make a list of censored words and replace that word by xxxxx.

with open(f"/Users/dartstorm/Desktop/Github/Python/Basics/censored.txt") as f:
    data = f.read()
censored_words = ["donkey", "lazy", "foolish"]
for word in censored_words:
    data = data.replace(word,"xxxxx")
#or
#new = data.replace("donkey","xxxxx").replace("lazy","xxxxx").replace("foolish","xxxxx")
with open(f"/Users/dartstorm/Desktop/Github/Python/Basics/censored.txt","w") as f:
    f.write(data)

"""
Paragraph: 

The donkey was carrying loads on the farm while a lazy worker watched.
Everyone thought it was foolish to ignore the hardworking donkey,
but the donkey continued doing its job without complaining.
Calling the effort lazy or foolish did not change how responsible the donkey really was.
"""

    
    
