# Write a python function which converts inches to cms

def inches_to_centimeters(inches):
    centimeters = inches * 2.54
    return centimeters

inches = int(input("Enter the Number : "))
centimeters = inches_to_centimeters(inches)
print(centimeters)
