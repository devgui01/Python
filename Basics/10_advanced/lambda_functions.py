# Before
def add(a, b):
    sum = a + b
    return sum
a = add(2, 9)
print(a)

def Square(a):
    S = a * a
    return S
a = Square(9)
print(a)


# After
sum = lambda a, b: a + b
print(sum(1, 10))

square = lambda a: a * a
print(square(9))
