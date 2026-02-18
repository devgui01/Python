numbers_list = [1, 2, 9, 5, 3, 5]
squared_list = []
for number in numbers_list:
    squared_list.append(number * number)
print(squared_list)

# [new_value for item in list if condition]

squared_numbers = [number * number for number in numbers_list]  # Using List Comprehensions
print(squared_numbers)
