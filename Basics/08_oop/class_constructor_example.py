class Animal:
    legs_count = 2
    hands_count = 2
    power_level = 100

    def __init__(self, strength, health, attack_power): #Dunder Method in Python Which is automatically Called
        self.strength = strength
        self.health = health
        self.attack = attack_power
        print(f"\n\tLoading ...")
        print(f"Strength is : {strength}\nHealth is : {health}\nAttack is : {attack_power}")

kangaroo = Animal(100, 12, "100x")
"""
strength_input = int(input("Enter Your Strength ?/100 : "))
health_input = int(input("Enter Your Health ?/100 : "))
attack_input = input("Enter Your Attack Name  : ")
"""
