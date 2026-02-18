"""
Store the multiplication tables in a file named Tables.txt.
"""
l1 = [2,4,6,8,10,12,14,16,18,20]
with open("/Users/dartstorm/Desktop/Github/Python/Basics/Tables.py","w") as f:
    for item in l1:
        f.write(str(f"{item}\t"))
    
with open("/Users/dartstorm/Desktop/Github/Python/Basics/Tables.py") as w:
    print(w.read())


