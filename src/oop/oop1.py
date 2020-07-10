# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    def __init__(self):
        pass
        # main class


class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()
# from vehicle


class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
# from groundvehicle


class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
# from groundvehicle


class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()
    # from vehicle


class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()


class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()

        # from flightvehicle
