# learn unpacking , Concatination , and Arthimatic Operations With type conversion & Type Checking

# Unpacking
unpacking = ['apple', 'banana', 'cherry']
x, y, z = unpacking
print(x)
print(y)
print(z)

# Concatination
x = "My name is "
y = "Muhammad Moeed"
z = x + y
print(z)

# Arthimatic Operations With type conversion

# Task : Find area of square and area of rectangle 
areaOfSquare = int(input("Enter the side of square : "))
areaOfRectangle = int(input("Enter the length of rectangle : "))

Area = areaOfSquare**2
Rectangle = 2 * areaOfRectangle

print("Area of Square is : ", Area)
print("Area of Rectangle is : ", Rectangle)

# Arthematic Operations
addition = Area + Rectangle
subtraction = Area - Rectangle
multiplication = Area * Rectangle
division = Area / Rectangle
modulus = Area % Rectangle
exponent = Area ** Rectangle
floorDivision = Area // Rectangle

print("Addition is : ", addition)
print("Subtraction is : ", subtraction)
print("Multiplication is : ", multiplication)
print("Division is : ", division)
print("Modulus is : ", modulus)
print("Exponent is : ", exponent)
print("Floor Division is : ", floorDivision)

# Type Checking
print(type(areaOfSquare))
print(type(areaOfRectangle))

# Type Conversion
areaOfSquare = str(areaOfSquare)
areaOfRectangle = str(areaOfRectangle)

print(type(areaOfSquare))
print(type(areaOfRectangle))





