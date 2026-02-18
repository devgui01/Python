"""
Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways.
"""


import random

class Train:
    def __init__(self, fro, to, tn):
        self.fro = fro
        self.to = to
        self.tn = tn
        self.booked = False
        self.seats = random.randint(1, 100)

    def book(self):
        if self.seats > 0:
            self.booked = True
            self.seats -= 1
            print(f"\nTicket Booked Successfully!")
            print(f"Train No : {self.tn}")
            print(f"From {self.fro} to {self.to}")
        else:
            print("\nNo seats available!")

    def status(self):
        late = random.randint(0, 5)
        if late == 0:
            run_status = "Train is on time"
        else:
            run_status = f"Train is {late} hours late"

        print(f"\nTrain No : {self.tn}")
        print(f"Seats Available : {self.seats}")
        print(run_status)

    def fare(self):
        fare = random.randint(100, 1000)
        print(f"\nTrain No : {self.tn}")
        print(f"Fare : ₹{fare}")

    @staticmethod
    def wrong():
        print("Invalid Choice")


a = input("Departure Station : ")
b = input("Destination Station : ")
c = int(input("Enter Train Number : "))

Passenger = Train(a, b, c)

while True:
    d = int(input("\n1. Book Ticket\n2. Check Status\n3. Check Fare\n4. Exit\nEnter Choice : "))

    if d == 1:
        Passenger.book()
    elif d == 2:
        Passenger.status()
    elif d == 3:
        Passenger.fare()
    elif d == 4:
        break
    else:
        Train.wrong()

