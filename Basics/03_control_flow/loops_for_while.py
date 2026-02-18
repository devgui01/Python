# For Loops
for iteration in range(1, 11):
    print("Hello World", iteration)
print("Start of For Loop_____________________________")


items_list = ["ram", False, True, "Radhe", "Gather", 222222]
# For Lists
for item in items_list:
    print(item)

for index in range(len(items_list)):
    print(items_list[index])
print("End of For Loop_____________________________Lists")


tuple_items = ("ram", False, True, "Radhe", "Gather", 222222)
# For Tuple
for index in range(len(tuple_items)):
    print(tuple_items[index])

for item in tuple_items:
    print(item)
print("End of For Loop_____________________________Tuples")


string_tuple = "ram", "Radhe", "Gather"
# For Strings
for index in range(len(string_tuple)):
    print(string_tuple[index])

for item in string_tuple:
    print(item)
print("End of For Loop_____________________________Strings")

# Using Break, Continue and Pass
for number in range(11):
    if number == 5:
        break
    print(number)
print("End of For Loop_____________________________Break")

# Continue - skip current iteration
for number in range(11):
    if number == 5:
        continue
    print(number)
print("End of For Loop_____________________________Continue")

# Pass - null statement
for number in range(11):
    if number == 5:
        pass
print("End of For Loop_____________________________Pass")

# Else in for loop
for number in range(21):
    print(number)
else:
    print("Printed till 21")
print("End of For Loop_____________________________Else")


# While Loops
counter = 1
while counter < 11:
    print("Hello World", counter)
    counter = counter + 1
print("End of While Loop_____________________________")
