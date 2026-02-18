"""Write a python program to rename a file to “renamed_by_ python.txt."""


def rename(a,b): #a-->Before Renamed file b-->After Renamed File
    with open(f"/Users/dartstorm/Desktop/Github/Python/Basics/{a}","r") as i:
        data = i.read()
    print(f"\t\tWorking !!!")
    with open(f"/Users/dartstorm/Desktop/Github/Python/Basics/{b}","w") as f:
        f.write(data)
    print(f"\t\t Work Done !!!")
    

rename(a=input("Enter the File Name You wanna to Rename : "),b=input("Enter the Name you have to give to the file : "))