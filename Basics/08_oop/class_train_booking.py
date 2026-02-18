"""
Write a Class 'Train' which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways.
"""


import random

class Train:
    def __init__(self, departure_station, destination_station, train_number):
        self.departure = departure_station
        self.destination = destination_station
        self.train_number = train_number
        self.is_booked = False
        self.available_seats = random.randint(1, 100)

    def book_ticket(self):
        if self.available_seats > 0:
            self.is_booked = True
            self.available_seats -= 1
            print(f"\nTicket Booked Successfully!")
            print(f"Train No : {self.train_number}")
            print(f"From {self.departure} to {self.destination}")
        else:
            print("\nNo seats available!")

    def get_status(self):
        delay_hours = random.randint(0, 5)
        if delay_hours == 0:
            train_status = "Train is on time"
        else:
            train_status = f"Train is {delay_hours} hours late"

        print(f"\nTrain No : {self.train_number}")
        print(f"Seats Available : {self.available_seats}")
        print(train_status)

    def get_fare(self):
        fare_amount = random.randint(100, 1000)
        print(f"\nTrain No : {self.train_number}")
        print(f"Fare : ₹{fare_amount}")

    @staticmethod
    def invalid_choice():
        print("Invalid Choice")


departure_input = input("Departure Station : ")
destination_input = input("Destination Station : ")
train_number_input = int(input("Enter Train Number : "))

passenger = Train(departure_input, destination_input, train_number_input)

while True:
    user_choice = int(input("\n1. Book Ticket\n2. Check Status\n3. Check Fare\n4. Exit\nEnter Choice : "))

    if user_choice == 1:
        passenger.book_ticket()
    elif user_choice == 2:
        passenger.get_status()
    elif user_choice == 3:
        passenger.get_fare()
    elif user_choice == 4:
        break
    else:
        Train.invalid_choice()
