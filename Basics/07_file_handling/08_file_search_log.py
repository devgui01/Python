# Write a program to mine a log file and find if it contains 'python' and on which line.

with open("logfile.txt", "r") as f:
    data = f.readlines()
    line = 1
    for words in data:
        if "python" in words:
            print(f"Line No: {line}")
            break
        line += 1
    else:
        print("Python Is Not Present in the above Para!")

# Alternative method (commented):
# with open("logfile.txt", "r") as f:
#     data = f.read()
#     if "python" in data.lower():
#         print("This Log-File Contains Python")
#     else:
#         print("It doesn't Contain Python")

""" Sample Log
[INFO] System started successfully
[WARNING] Low memory detected
[INFO] User logged in
[ERROR] python module failed to load
[INFO] System shutting down
"""