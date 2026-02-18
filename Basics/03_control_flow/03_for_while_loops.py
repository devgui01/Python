# For Loops
for i in range(1, 11):
    print("Hello World", i)
print("Start of For Loop_____________________________")


l1 = ["ram", False, True, "Radhe", "Gather", 222222]
# For Lists
for i in l1:
    print(i)

for i in range(len(l1)):
    print(l1[i])
print("End of For Loop_____________________________Lists")


l2 = ("ram", False, True, "Radhe", "Gather", 222222)
# For Tuple
for i in range(len(l2)):
    print(l2[i])

for i in l2:
    print(i)
print("End of For Loop_____________________________Tuples")


l3 = "ram", "Radhe", "Gather"
# For Strings
for i in range(len(l3)):
    print(l3[i])

for i in l3:
    print(i)
print("End of For Loop_____________________________Strings")

# Using Break, Continue and Pass
for i in range(11):
    if i == 5:
        break
    print(i)
print("End of For Loop_____________________________Break")

# Continue - skip current iteration
for i in range(11):
    if i == 5:
        continue
    print(i)
print("End of For Loop_____________________________Continue")

# Pass - null statement
for i in range(11):
    if i == 5:
        pass
print("End of For Loop_____________________________Pass")

# Else in for loop
for i in range(21):
    print(i)
else:
    print("Printed till 21")
print("End of For Loop_____________________________Else")


# While Loops
i = 1
while i < 11:
    print("Hello World", i)
    i = i + 1
print("End of While Loop_____________________________")
