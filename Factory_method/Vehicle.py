from abc import ABCMeta, abstractstaticmethod

class IVehicle(metaclass=ABCMeta):
    """An abstract class of any means of transportation."""

    @abstractstaticmethod
    def vehicle_method():
        """An interface method."""

class Tank(IVehicle):
    """A class of any tank."""

    def __init__(self, model):
        self.model = model
    
    def vehicle_method(self):
        print(f'This type of tank is {self.model}')

class Jeep(IVehicle):
    """A class of any Jeep."""

    def __init__(self, model):
        self.model = model
    
    def vehicle_method(self):
        print(f'This type of Jeep is {self.model}')

class VehicleFactory:
    """A factory class."""

    @staticmethod
    def build_vehicle(vehicle_type, vehicle_model):
        if vehicle_type == 'Tank':
            return Tank(vehicle_model)
        if vehicle_type == 'Jeep':
            return Jeep(vehicle_model)
        raise Exception('This type of transportation does not exist.')

if __name__ == '__main__':
    selected_type = input("What type of transportation do you want to create?\n")
    selected_model = input("What model of transportation do you want to create?\n")

    selected_vehicle = VehicleFactory.build_vehicle(selected_type,selected_model)
    selected_vehicle.vehicle_method()