# Function , return statement , Parameters & Argument & Default Parameter & __doc__string

#Greet
def greet():
    print('Hello world')
    
greet()

# Multiplication of Two numbers
input1 = int(input('Enter any number'))
input2 = int(input('Enter any number'))
def product(num1,num2):
    print(f'Multiplication is : {num1 * num2}')
    
product(input1,input2)

#Print Two name With return Statement

firstName = input('Enter First Name')
lastName = input('Enter First Name')
def name(fName,lName):
    return f'Name : {fName} {lName}'

user1 = name(firstName,lastName)
print(user1)

# Default Parameter
Country = input('Enter country')
def country(count='pakistan'):
    return count

yourCountry = country()
print(yourCountry)

# Doc String 
def product(num_1,num_2):
    '''calculator product'''
    return num_1*num_2
answer=product(23,45)
print('answer=',answer)
print(product.__doc__)

# Product with Loop
def mul():
    products=0
    num_1=4
    num_2=3
    for x in range(1,num_1+1):
        products+=num_2
    print(products)
mul()


