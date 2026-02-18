class Planets:
    # Class attributes
    near_sun = False
    has_life = "Nope"
    power = 100

    def display_power(self):
        """Display the planet's power level."""
        print(self.power)

    @staticmethod
    def greet():
        """Greet the user - static method doesn't use self."""
        print("Good Morning")


# Create planet instances
neptune = Planets()
neptune.name = "Neptune"
neptune.has_life = "Not Possible"
neptune.power = 900
neptune.greet()
print(f"{neptune.name}:")
print(f"\tPower: {neptune.power}, Has Life: {neptune.has_life}, Near Sun: {neptune.near_sun}\n")

earth = Planets()
earth.name = "Earth"
earth.has_life = "Yes"
earth.near_sun = True
earth.greet()
print(f"{earth.name}:")
print(f"\tHas Life: {earth.has_life}, Near Sun: {earth.near_sun}\n")
