#Write a program to mine a log file and find out whether it contains ‘python’ and if contain then in which line it contain.


with open(f"/Users/dartstorm/Desktop/Github/Python/Basics/logfile.txt","r") as f:
    data = f.readlines()
    line = 1
    for words in data:
        if("python" in words): 
            print(f"Line NO : {line}")
            break
        line+=1
    else:
        print("Python Is NoT Present in the above Para !")
        
    
        








# with open(f"/Users/dartstorm/Desktop/Github/Python/Basics/logfile.txt","r") as f:
#     data = f.read()
#     if("python" in data.lower()):
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