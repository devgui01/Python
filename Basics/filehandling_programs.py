"""
1.Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’.
"""
with open("/Users/dartstorm/Desktop/Github/Python/Basics/poems.txt", "r") as f:
    for line in f:
        words = line.split()   # splits by spaces
        print(words)
