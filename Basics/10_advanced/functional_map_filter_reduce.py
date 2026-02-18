"""🔁 map → "change every item"
🚫 filter → "keep some items"
➕ reduce → "collapse into one"""


from functools import reduce
l1 = [1, 2, 3, 4, 5, 6]

# Example of Map
square = lambda a: a * a
a = map(square, l1)
print(list(a))


# Example of Filter
def even(n):
    if n % 2 == 0:
        return True
    return False
a = filter(even, l1)
print(list(a))

# Example of Reduce
sum = lambda a, b: a * b
print(reduce(sum, l1))
