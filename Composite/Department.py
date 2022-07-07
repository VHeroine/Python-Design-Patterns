from abc import ABCMeta, abstractmethod, abstractstaticmethod


class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, employees):
        """This constuctor will be implemented in child class."""

    @abstractstaticmethod
    def print_department():
        """"THis method will be implemented in child class."""


class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees
    
    def print_department(self):
        print(f"The number of accounting department employees: {self.employees}")


class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees
    
    def print_department(self):
        print(f"The number of development department employees: {self.employees}")


class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_departments = []

    def add(self, dept):
        self.sub_departments.append(dept)
        self.employees += dept.employees
    
    def print_department(self):
        print(f"The number of Parent Department employees: {self.base_employees}")
        for dept in self.sub_departments:
            dept.print_department()
        print(f"The total number of employees: {self.employees}")

dept1 = Accounting(100)
dept2 = Development(70)
dept3 = ParentDepartment(15)
dept3.add(dept1)
dept3.add(dept2)
dept3.print_department()