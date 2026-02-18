#Before Using emumerate
l1 = ["Hello",23,False,True,45,"Ram"]
index = 0
for item in l1:
    print(f"The item number at index {index} is {item}")
    index = index+1

# Using Enumerate

for index,item in enumerate(l1):
    print(f"The item number at index {index} is {item}")

