"""
Types of Inheritance:
1. Single Level: Parent > Child
2. Multi-Level: Parent > Child1 > Child2
3. Multiple: ParentA + ParentB > Child
"""


class LivingThings:
    isLive = True

    def CanHearSound(self):
        print("We Can Hear Sound")


class HumanBeings(LivingThings):  # Single Level Inheritance
    def Intelligent(self):
        print("Most Intelligent!")


class Animals(HumanBeings):  # Multi-Level Inheritance
    def Powerful(self):
        print("Powerful")
