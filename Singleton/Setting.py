from abc import ABCMeta, abstractstaticmethod

class ISetting(metaclass=ABCMeta):
    """This is an abstract interface of global setting."""

    @abstractstaticmethod
    def print_data():
        """This method will be implemented in a child class."""

class SettingSingleton(ISetting):

    __instance = None

    @staticmethod
    def get_instance():
        if SettingSingleton.__instance == None:
            SettingSingleton("Default name", None)
        return SettingSingleton.__instance
    
    def __init__(self, name, val) -> None:
        if SettingSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.name = name
            self.val = val
            SettingSingleton.__instance = self

    @staticmethod
    def print_data():
        print(f"Name: {SettingSingleton.__instance.name}, value: {SettingSingleton.__instance.val}")

setting_01 = SettingSingleton("Server_works", True)
print(setting_01)
setting_01.print_data()

# setting_02 = SettingSingleton("Server_stops", False) # This code will raise the exception.

setting_02 = SettingSingleton.get_instance()
print(setting_02)
setting_02.print_data()