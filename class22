# Task 1: 
# Create  a class point having two attributes x and y. (the two coordiantes of a point)
# and the following method:
# setx(xcoord):set the x coordinate or the pint to xcoord 
# sety(ycoord):sets the y coordinates of the point to y coord
# get():return x y value
#move (dx,dy):change the coordinate of the point type object from the current position (x,y) to (x+dx,y+dy)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def setx(self, xcoord):
        self.x = xcoord
    def sety(self, ycoord):
        self.y = ycoord
    def get(self):
        return self.x, self.y
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        
points = Point(1,2)
print(f'initial x value{points.x}')
print(f'initial y value{points.y}')
points.setx(67)
points.sety(56)
print(f'Set x value{points.x}')
print(f'Set y value{points.y}')

print(points.get())
points.move(23,54)
print(f'Addition x & dx value{points.x}')
print(f'Addition x & dy value{points.y}')
                    
                    
#create protected class
class ProtectedClass:
    def __init__(self):
        self._protected_var = 8
    def get_protected_var(self):
        return self._protected_var
    def set_protected_var(self, value):
        self._protected_var = value
        
protected_obj = ProtectedClass()
print(protected_obj.get_protected_var()) 
protected_obj.set_protected_var(10)
print(protected_obj.get_protected_var())  

#create Private class
class PrivateClass:
    def __init__(self,x):
        self.__private_var = x
    def get_private_var(self):
        return self.__private_var
    def set_private_var(self, value):
        self._private_var = value
        
protected_obj = PrivateClass(6)
print(protected_obj.get_private_var()) 
protected_obj.set_private_var(10)
print(protected_obj.get_private_var())  
        
        
    


        

