"""
Write a program to input name, marks and phone number of a student and format it
using the format function like below:
"The name of the student is Harry, his marks are 72 and phone number is 99999888"
"""

student_name = input("Enter Your Name : ")
student_marks = input("Enter the Marks : ")
student_phone = int(input("Enter Your Phone Number : "))
print("The name of the student is {}, his marks are {} and phone number is {}".format(student_name, student_marks, student_phone))
