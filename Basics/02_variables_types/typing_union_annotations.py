#Maybe the Program not work but you just see the types like how union used in the program by import typing

from typing import List, Union, Tuple
def sum_values(first_value: Union[int, str], second_value: int) -> int:
    total = first_value + second_value
    return total
result = sum_values(2, 3)
print(result)



number: int = 5
name: str = "Harry"
def  add_numbers(first_num: int, second_num: int) -> int:
    return first_num + second_num
