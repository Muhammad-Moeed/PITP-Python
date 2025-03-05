# class operation:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,y):
#         return (self.x+y)
# x+y -->x.__add__(y)
# x+y -->x.__mul__(y)
# print(5+9) #5.__add__(9)    
        
# class Mystr:
#     def __init__(self, x):
#         self.x = x
#     def __add__(self, y):
#         return (f'{self.x} is added with {y} = {self.x+y}')
# x=Mystr(5)
# print(x+9)



# class Mystr:
#     def __init__(self, x):
#         self.x = x
#     def __add__(self, y):
#         return (f'{self.x} is added with {y} = {self.x+y}')
#     def __sub__(self, y):
#         return (f'{self.x} is sub with {y} = {self.x-y}')
#     def __mul__(self, y):
#         return (f'{self.x} is multi with {y} = {self.x*y}')
#     def __truediv__(self, y):
#         return (f'{self.x} is divide with {y} = {self.x/y}')
# x_input=int(input('enter first number'))
# y_input=int(input('enter secound number'))
# y=y_input     
# x=Mystr(x_input)
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)

class salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
    def annual_salary(self):
        return (self.pay* 12) + self.bonus

class Eployeeone:
    def __init__(self, name , age, sal):
        self.name = name
        self.age = age
        self.agg_salary = sal

    def total_sal(self):
        return self.agg_salary.annual_salary()
    
salary=salary(10000,1500)
emp=Eployeeone ('Geek',25,salary) 
print(emp.total_sal())