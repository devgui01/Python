"""
1.Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’ if Found count it.
"""

with open("/Users/dartstorm/Desktop/Github/Python/Basics/poems.txt") as f:
    data = f.read().lower()
    count = data.count("twinkle")
    if("twinkle" in data):      
        twinkle = f"Twinkle Found {count} times"
    else:
        twinkle = "Twinkle not Found"
    print(twinkle)



        
    
      
