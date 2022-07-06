from abc import ABCMeta, abstractstaticmethod
import time
import os


class IPerson(metaclass=ABCMeta):
    """Interface class."""

    @abstractstaticmethod
    def person_method():
        """Interface method."""


class Person(IPerson):

    def person_method(self, name):
        self.name = name
        print(f"I am {self.name}.")


class ProxyPerson(IPerson):

    def __init__(self):
        self.person = Person()
    
    def loggin(self, name, file_name='log.txt'):
        with open(file_name, 'a') as f:
            f.write(f'{time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())} - {name} was logged to the system.')
    
    def person_method(self, name):
        self.loggin(name)
        self.person.person_method(name)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    person_name = input("What is your name? ")
    p1 = Person()
    p1.person_method(person_name) # This call will not be logged.

    p2 = ProxyPerson()
    p2.person_method(person_name) # This call will be logged because of Proxy design pattern.