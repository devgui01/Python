"""
Write a program to generate multiplication tables from 2 to 20 and write it to the
different files. Place these files in a folder for a 13 – year old.
"""



inp = 1
for j in range(2,21):
    inp+=1
    with open(f"/Users/dartstorm/Desktop/Github/Python/Basics/tables/Table of {inp}","w") as f:
        for i in range(1,11):
            f.write(f"{inp} * {i} = {inp*i}\n")
