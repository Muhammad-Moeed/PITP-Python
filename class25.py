# Create a class student with private attributes name ,age,grade,
# Implemet methods for setting and getting these attributes .
# Ensure that the grade can only be accessed via getter and setter method


class Student():
    def __init__(self,n,a,g):
        self.__name = n
        self.__age = a
        self.__grade = g
    def get(self):
        return f'{self.__name} {self.__age} {self.__grade}'
    def set(self,n,a,g):
        self.__name = n
        self.__age = n
        self.__grade = n
        
CLass1 = Student('Moeed',16,'b')
CLass1.get()  
CLass1.set('Ali',12,'A')
CLass1.get()

# create an abstract class Employee with an abstract method calculate_salary().
# Then,Create a subclass Manager with a method calculate_salary() 
# that returns the manager's salary based on some logic.Demonstrate usage
from abc import abstractmethod

class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @abstractmethod
    def calculate_salary(self):
        pass
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    def calculate_salary(self):
        return self.salary + self.bonus
Manager1 = Manager('Moeed', 10000, 5000)
print(Manager1.calculate_salary())
                
    
        
        
           
           
        