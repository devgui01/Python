"""Write a python program to rename a file."""


def rename_file(source_file, destination_file):
    """Copy content from source file to destination file"""
    with open(source_file, "r") as source_handle:
        file_data = source_handle.read()
    print("\t\tWorking !!!")
    with open(destination_file, "w") as destination_handle:
        destination_handle.write(file_data)
    print("\t\tWork Done !!!")


rename_file(
    source_file=input("Enter the File Name You wanna to Rename: "),
    destination_file=input("Enter the New File Name: ")
)
