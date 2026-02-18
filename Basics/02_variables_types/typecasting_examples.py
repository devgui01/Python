print("1.")
string_value = "12.009"  #String
float_value = float(string_value)  #String to Float
print(type(float_value))

print("2.")
invalid_string = "12b"  #String
"""float_value = float(invalid_string) """ #Error-Occured @TypeError
print(type(float_value))

print("3.")
numeric_string = "123"
integer_value = int(numeric_string)
print(type(integer_value))
