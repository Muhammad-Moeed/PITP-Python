# Types of Methods 
class myClass:
    classAttribute='ClassAttributre'
    
    def __init__(self):
        self.instanceAttribute='InstanceAttribute'
        
    #Intance Methods
    def instanceMethod(self):
        print(myClass.classAttribute)
        print(self.instanceAttribute)
        print('This is an instance method')
    
    # ClassMethod
    @classmethod
    def classMethod(cls):
        print(cls.classAttribute)
        # print(self.instanceAttribute) Error
        # print(cls.instanceAttribute) Error
        print('This is a class method')
        
    # ClassMethod  
    @staticmethod
    def staticMethod():
        print(myClass.classAttribute)
        # print(self.instanceAttribute) Error
        # print(cls.instanceAttribute) Error
        print('This is a static method')
        
    # Another Metohd
    def anotherMethod(self):
        # self.instanceMetoh() Error
        # myClass.instanceMetoh() Error
        print('This is another method')
        
executeMyClass = myClass()
executeMyClass.instanceMethod()
myClass.classMethod()
myClass.staticMethod()
executeMyClass.anotherMethod()


# ****************Abstract Class****************
from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod
    def noOfSides(self):
        pass
        # print('I am a type of polygon') #Implementtation
class Square(Polygon):
    def noOfSides(self):
        # super().noOfSides() #Call Parent Method
        print('I Have 4 sides')
class Triangle(Polygon):
    def noOfSides(self):
        print('I Have 3 sides')


# ExecutePolygon = Polygon() Error Because this is no directly cretae object
# print(ExecutePolygon)
ExecuteSuqare = Square()
ExecuteSuqare.noOfSides()
ExecuteTriangle = Triangle()
ExecuteTriangle.noOfSides()

    