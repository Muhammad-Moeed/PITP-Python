# Learn Multi Line String, 
# String Length , 
# Check word from sring , 
# (Slicing)[start:end:direction/stepsize] , Mutable and Immutable String 
# Task solve Quadratic Euqation with formula -b±√b²-4ac/2a

# Multi Line String
multiLine = """This is a 
multi line string """
print(multiLine)

# String Length
string = "Hello World"
print(len(string))

# Check word from string
string = "Hello World"
print("Hello" in string)

# Slicing
string = "COMPUTER"
print(string[1:4]) # slice from 1 to 4
print(string[:4]) # slice from 0 to 4
print(string[4:]) # slice from 4 to end
print(string[:]) # slice from 0 to end
print(string[1:4:2]) # slice from 1 to 4 with step 2
print(string[::2]) # slice from 0 to end with step 2
print(string[::-1]) # reverse the string
print(string[-1:-5:-1]) # slice from -1 to -5 with step -1
print(string[::-2]) # reverse the string with step 2

# Mutable and Immutable String
string = "COMPUTER" # string[1] = "A" # Error because string is immutable

# => Task solve Quadratic Euqation with formula -b±√b²-4ac/2a
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = (b**2) - (4*a*c)
sol1 = (-b - d**0.5) / (2*a)
sol2 = (-b + d**0.5) / (2*a)

print("Solution 1: ", sol1)
print("Solution 2: ", sol2)


