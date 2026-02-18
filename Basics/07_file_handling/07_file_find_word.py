"""
Read text from 'poems.txt' and find if it contains the word 'twinkle'.
Count occurrences if found.
"""

with open("poems.txt") as f:
    data = f.read().lower()
    count = data.count("twinkle")
    if "twinkle" in data:
        print(f"Twinkle Found {count} times")
    else:
        print("Twinkle not Found")



        
    
      
