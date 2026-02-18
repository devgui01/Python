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
        self.booked = False
        self.seats = random.randint(1, 100)

    def book(self):
        if self.seats > 0:
            self.booked = True
            self.seats -= 1
            print(f"\nTicket Booked Successfully!")
            print(f"Train No : {self.train_number}")
            print(f"From {self.departure} to {self.destination}")
        else:
            print("\nNo seats available!")

    def status(self):
        late = random.randint(0, 5)
        if late == 0:
            run_status = "Train is on time"
        else:
            run_status = f"Train is {late} hours late"

        print(f"\nTrain No : {self.train_number}")
        print(f"Seats Available : {self.seats}")
        print(run_status)

    def fare(self):
        fare = random.randint(100, 1000)
        print(f"\nTrain No : {self.train_number}")
        print(f"Fare : ₹{fare}")

    @staticmethod
    def wrong():
        print("Invalid Choice")


departure_station = input("Departure Station : ")
destination_station = input("Destination Station : ")
train_number = int(input("Enter Train Number : "))

Passenger = Train(departure_station, destination_station, train_number)

while True:
    user_choice = int(input("\n1. Book Ticket\n2. Check Status\n3. Check Fare\n4. Exit\nEnter Choice : "))

    if user_choice == 1:
        Passenger.book()
    elif user_choice == 2:
        Passenger.status()
    elif user_choice == 3:
        Passenger.fare()
    elif user_choice == 4:
        break
    else:
        Train.wrong()

