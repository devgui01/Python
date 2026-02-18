"""
Write a program to input name, marks and phone number of a student and format it
using the format function like below:
“The name of the student is Harry, his marks are 72 and phone number is 99999888”
"""

n = input("Enter Your Name : ")
m = input("Enter the Marks : ")
p = int(input("Enter Your Phone Number : "))
print("The name of the student is {}, his marks are {} and phone number is {}".format(n,m,p))