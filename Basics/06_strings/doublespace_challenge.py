# 1.Write a program to detect double space in a string.
input_string = input("Enter a String : ")  #UserInput


"""if it returns -1 means there is no double space in the given string but,
                                                           if there is double space it returns teh index of the double space"""
print(input_string.find("  "))


#2.Write a program to Detect and Count double space in a string.

input_string = input("Enter a String : ")  #UserInput
double_space_count = input_string.count("  ") #Counts the Spaces


#Print how many double-spaces occur's in the user-defined input_string.
print(f"In Your String there is {double_space_count} double Spaces !")


#3.Replace the double space from problem 3 with single spaces.

input_string = input("Enter a String : ")  #UserInput
replaced_string = input_string.replace("  "," ") #Counts the double spaces and replace with single Spaces
print(replaced_string) #Prints the output
