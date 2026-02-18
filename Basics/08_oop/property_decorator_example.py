class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks   # underscore means "private" by convention

    # Getter
    @property
    def marks(self):
        return self._marks

    # Setter
    @marks.setter
    def marks(self, value):
        if value < 0 or value > 100:
            print("Marks must be between 0 and 100")
        else:
            self._marks = value


# Create object
s1 = Student("Pritam", 85)

# Access value (getter is called)
print("Marks:", s1.marks)

# Modify value (setter is called)
s1.marks = 95
print("Updated Marks:", s1.marks)

# Invalid update
s1.marks = 120
