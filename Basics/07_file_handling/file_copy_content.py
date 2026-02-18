# Write a program to make a copy of a text file “this.txt” in "pcopy.txt"

def copy(a): #1.kya copy 2.kisme copy
    copymaal = a
    return copymaal

with open(f"/Users/dartstorm/Desktop/Github/Python/Basics/this.txt","r") as f:
    data = f.read()
    
dat = copy(data)

with open(f"/Users/dartstorm/Desktop/Github/Python/Basics/pcopy.txt","w") as f:
    f.write(dat)









    