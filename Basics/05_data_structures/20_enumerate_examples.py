"""
Write a program to print third, fifth and seventh element from a list using enumerate
function.
"""

l1 = [12,23,45,"Hello","Raj Shamani","Mr Beast","Virat kohli","Dhoni","Ben 10"]
for index,item in enumerate(l1):
    if index==2 or index==4 or index==6:
        print(f"Index : {index},Values : {item}")