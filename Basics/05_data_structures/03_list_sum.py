# Write a program to sum a list with 4 numbers.

#Complex Method 

l1 =[12,12,12,34] #Empty List
""" 
Pop each element and return its value & simultaneouly store for all four numbers and store in addlist Variable
"""
addlist= l1.pop() + l1.pop() + l1.pop() + l1.pop() 
print(f"Sum of Elements : {addlist}") #Print Addlist Variable
print(l1) #Print the Original List



#                                            Or

#Simple Build-In-Method

l = [12,12,12,12,12]
print(sum(l))