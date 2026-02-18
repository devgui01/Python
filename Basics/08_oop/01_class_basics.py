class Planets:
    nearSun = False  # Class attribute
    isLifeexist = "Nope"
    power = 100

    def Power(self):
        print(self.power)

    @staticmethod  # Static method - use when we don't use self
    def Greet():
        print("Good Morning")


Neptune = Planets()
# Neptune.Power()  # Both are same
# Planets.Power(Neptune)

Neptune.planet = "Neptune"  # Object/instance attribute
Neptune.isLifeexist = "Not Possible"  # Overwrite class attribute
Neptune.power = 900
Neptune.Greet()
print(f"{Neptune.planet}:")
print(f"\tPower: {Neptune.power}, IsLifeExitsHere: {Neptune.isLifeexist}, PlanetIsNearSun: {Neptune.nearSun}\n")

Earth = Planets()
Earth.planet = "Earth"  # Object/instance attribute
Earth.isLifeexist = "Yes"  # Overwrite class attribute
Earth.nearSun = True  # Overwrite class attribute
Earth.Greet()
print(f"{Earth.planet}:")
print(f"\tIsLifeExitsHere: {Earth.isLifeexist}, PlanetIsNearSun: {Earth.nearSun}\n")
