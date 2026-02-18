#Function With Arguments and Using of Return

def calculate_sum(first_num, second_num, message):
    total = first_num + second_num
    return f"{total} {message}"

result = calculate_sum(message="kidding", first_num=3, second_num=4)
print(result)
