"""Write a python program to rename a file."""


def rename(source, destination):
    """Copy content from source file to destination file"""
    with open(source, "r") as i:
        data = i.read()
    print("\t\tWorking !!!")
    with open(destination, "w") as f:
        f.write(data)
    print("\t\tWork Done !!!")


rename(
    source=input("Enter the File Name You wanna to Rename: "),
    destination=input("Enter the New File Name: ")
)
