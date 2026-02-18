"""
A file contains a word “Donkey” multiple times. You need to write a program
which replace this word with ##### by updating the same file. 
"""


with open(f"/Users/dartstorm/Desktop/Github/Python/Basics/donkey.txt") as f:
    text = f.read()
final = text.replace("donkey","#####")
with open(f"/Users/dartstorm/Desktop/Github/Python/Basics/donkey.txt","w") as j:
    j.write(final)


"""
Paragraph:

The donkey is a hardworking animal, and the donkey has been helping humans for centuries.
In villages, the donkey carries heavy loads where machines cannot go.
A donkey may look slow, but the donkey is patient and strong.
People often underestimate the donkey, yet the donkey continues to work quietly without complaint.
From farms to mountains, the donkey remains a loyal and useful animal.

"""
        
        