class LivingThings:
    life_indicator = 122

    def __init__(self):
        super().__init__() #Call My Father (: (super().__init__() is used in a child class to call the constructor of its parent class so that parent class data members are initialized.)
        print(f"LivingThings Constructor Called ! ")

    @classmethod #--->The @classmethod decorator is used to work with class variables (class values) using the class (cls) instead of instance variables (self).
    def can_hear_sound(cls):
        print(f"We Are Hear Sound {cls.life_indicator}")

class HumanBeings(LivingThings):

    def __init__(self):
        super().__init__()
        print("HumanBeings Constructor Called !")

    def is_intelligent():
        print("Most Intelligent ? ")

class Animals(HumanBeings):

    def __init__(self):
        super().__init__()
        print("Animals Constructor Called !")

    def is_powerful():
        print("Powerful")

ram = LivingThings()
ram.life_indicator = 12
ram.can_hear_sound()
