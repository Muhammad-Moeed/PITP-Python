# Function Practical Problrms & Calculator program using Function

# 01 : Write python function htat accepts a string amd count the number of upper case and lower case letter
def count_string(string):
    countup = 0
    countlower = 0
    for i in string:
        if i.isupper():
            countup+=1
        else :
            countlower+=1
    print(f'Total Upper Number : {countup}')
    print(f'Total Lower Case : {countlower}')
strArg = 'Hello world'
count_string(strArg)

# 02 : Write python function to create a simple calculator .

num1 = int(input('Enter 1st number '))
num2 = int(input('Enter 2nd number '))
operator = (input('operation can you perform '))
def calculator():
    
    def Addition(a,b,c):
      add = a + b
      print(f'Addition : {add}')

    def Substraction(a,b,c):
      add = a - b
      print(f'Substraction : {add}')
      
    def Multiplication(a,b,c):
      add = a * b
      print(f'Multiplication : {add}')
      
    def Division(a,b,c):
      add = a / b
      print(f'Division : {add}')
    
    if operator =='+':
        Addition(num1,num2,operator)
    elif operator =='-':
        Substraction(num1,num2,operator)    
    elif operator =='*':
        Multiplication(num1,num2,operator)
    elif operator =='/':
        Division(num1,num2,operator)
    else:
        print('Invlalid Operation')
calculator()


