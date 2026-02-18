global_value = 1000
def modify_global():
    global global_value #The global keyword allows a function to modify a global variable.
    global_value = 12
    print(global_value)

modify_global()
print(global_value)
