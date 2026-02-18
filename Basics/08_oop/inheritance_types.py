"""
Types of Inheritance:
1. Single Level: Parent > Child
2. Multi-Level: Parent > Child1 > Child2
3. Multiple: ParentA + ParentB > Child
"""


class LivingThings:
    is_live = True

    def can_hear_sound(self):
        print("We Can Hear Sound")


class HumanBeings(LivingThings):  # Single Level Inheritance
    def is_intelligent(self):
        print("Most Intelligent!")


class Animals(HumanBeings):  # Multi-Level Inheritance
    def is_powerful(self):
        print("Powerful")
