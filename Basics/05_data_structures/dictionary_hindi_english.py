# Write a program to create a dictionary of Hindi words with values as their English translation.
# Provide user with an option to look it up!


# Concept 1 to do : (easy to understand) " Takes two input() from user "
d1 = {"Bhagwaan":"God","Kalyan":"Growth","Seb":"Apple","Kela":"Banana","Tufan ka Devta":"God of Thunder ? Thor"}
dinput = input("Enter a Hindi Word : ")
dhinput = input("Enter the English word for that hindi Word : ")
d1.update({dinput:dhinput})
print(d1)

# Concept 2 to do :(complex) " Takes Single input but takes both hindi-english translation words"
d1 = {"Bhagwaan":"God","Kalyan":"Growth","Seb":"Apple","Kela":"Banana","Tufan ka Devta":"God of Thunder ? Thor"} # A Dictionary
dinput = input("Enter a Hindi Word and also give its English translation : ") #Takes input() from user 
sp = dinput.split(" ").pop(0) #if the user gives "ram" and "shyam" then this split make it list of strings then the pop() delete the first element and return it and we just capture that return value and store it in a variable 
ps = dinput.split(" ").pop(1) #same for second variable
d1.update({sp:ps}) #Just put the stored values in the update position 
print(d1) #Print the dictionary 
