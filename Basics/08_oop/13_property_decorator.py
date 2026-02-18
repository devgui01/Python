class Employee:
    class_attribute_a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.class_attribute_a}")

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @name.setter
    def name(self, value):
        self.first_name = value.split(" ")[0]
        self.last_name = value.split(" ")[1]


employee = Employee()
employee.class_attribute_a = 45

employee.name = "Your Name"
print(employee.first_name, employee.last_name)

employee.show()
