# Write a program to accept marks of 6 students and display them in a sorted manner

student1_marks = int(input("Enter Your Marks  : "))
student2_marks = int(input("Enter Your Marks  : "))
student3_marks = int(input("Enter Your Marks  : "))
student4_marks = int(input("Enter Your Marks  : "))
student5_marks = int(input("Enter Your Marks  : "))
student6_marks = int(input("Enter Your Marks  : "))
marks_list = []
marks_list.append(student1_marks)
marks_list.append(student2_marks)
marks_list.append(student3_marks)
marks_list.append(student4_marks)
marks_list.append(student5_marks)
marks_list.append(student6_marks)
marks_list.sort()
print(marks_list)
