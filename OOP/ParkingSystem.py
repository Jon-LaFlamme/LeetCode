"""
Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:

ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, 
which are represented by 1, 2, and 3 respectively. A car can only park in a par
"""

#Note: explanation did not explicity say to decrement the lot spaces when parking, but that is expected
#Solved in ~7 minutes
#Cannot optimize further. Init is O(n) params and car_add call is O(1)

def __init__(self, big: int, medium: int, small: int):
    self.lot = {1: big, 2: medium, 3: small}   

def addCar(self, carType: int) -> bool:
    # big=1, med=2, small=3
    if self.lot[carType] > 0:
        self.lot[carType] -= 1
        return True
    else:
        return False

