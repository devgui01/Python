class Planets:
    is_near_sun = False  # Class attribute
    is_life_exist = "Nope"
    power_level = 100

    def display_power(self):
        print(self.power_level)

    @staticmethod  # Static method - use when we don't use self
    def greet_message():
        print("Good Morning")


neptune = Planets()
# neptune.display_power()  # Both are same
# Planets.display_power(neptune)

neptune.planet_name = "Neptune"  # Object/instance attribute
neptune.is_life_exist = "Not Possible"  # Overwrite class attribute
neptune.power_level = 900
neptune.greet_message()
print(f"{neptune.planet_name}:")
print(f"\tPower: {neptune.power_level}, IsLifeExitsHere: {neptune.is_life_exist}, PlanetIsNearSun: {neptune.is_near_sun}\n")

earth = Planets()
earth.planet_name = "Earth"  # Object/instance attribute
earth.is_life_exist = "Yes"  # Overwrite class attribute
earth.is_near_sun = True  # Overwrite class attribute
earth.greet_message()
print(f"{earth.planet_name}:")
print(f"\tIsLifeExitsHere: {earth.is_life_exist}, PlanetIsNearSun: {earth.is_near_sun}\n")
