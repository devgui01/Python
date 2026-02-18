"""
Question1.Write a class ‘Complex’ to represent complex numbers, along with overloaded
operators ‘+’ and ‘*’ which adds and multiplies them.
"""

class Complex():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self,c1):
        return Complex(self.a + c1.a , self.b + c1.b)
    
    def __str__(self):
        return f"{self.a} + {self.b}i"
    
Cn = Complex(1,2)
Cy = Complex(3,4)
print(Cn + Cy)
