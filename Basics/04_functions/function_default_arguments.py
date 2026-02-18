#Default Arguments

def calculate_sum(first_num, second_num, message="All is Well"):
    total = first_num + second_num
    return f"Your Sum is : {total} and {message}"

result = (calculate_sum(24, 36))
print(result)
