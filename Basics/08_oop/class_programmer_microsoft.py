"""
Create a class "Programmer" for storing information of few programmers
working at Microsoft.
"""

class Programmer:
    Company = "Microsoft"
    Salary = 200000

    def __init__(self, programmer_name):
        self.name = programmer_name

rajvir = Programmer("Rajvir")
print(f"\nProgrammer name : {rajvir.name}  Programmer Salary : {rajvir.Salary + 10000} \t Working at {rajvir.Company}\n")

raju = Programmer("Raju")
print(f"Programmer name : {raju.name} \t Programmer Salary : {raju.Salary + 800} \t Working at {raju.Company}\n")
