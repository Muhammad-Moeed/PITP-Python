# Decision Making & Conditional Operator (If , Elif , Else & Nested )

    # Task 01 : 
        # Write a programm to print 'Fizz' if a number is divisible by 3 , 'Buzz'
        # if its divisible by 5 , and 'fizz buzz 'if its divisible by bith 

number = int(input("Enter any number"))

if number%3 == 0 :
 print('Fizz')
elif number%5 == 0 :
 print('Buzz')
elif number%3 == 0 and number%5 ==0:
 print('FizzbBuzz')

    # Task 02 : 
        # write a student grading system,which take total marks input from the student and assign. 

totalMarks = int(input("Enter your total marks"))
if totalMarks > 90 and totalMarks < 100:
 print('A+')
elif totalMarks > 80 and totalMarks < 90:
 print('A')
elif totalMarks > 70 and totalMarks < 80:
 print('B')
elif totalMarks > 60 and totalMarks < 70:
 print('C')
elif totalMarks > 50 and totalMarks < 60:
 print('D')
else:
 print('F')

    # Task 03 : 
        # > Asks user for the total price of their shopping (Float)
        # > Asks if the customer is a student or not (yes/no)
        # > if they are a student,give them a 10% discount on their total price (a-(a*0.1))
        # > if the customer is not a student , give them 5% disocunt (a-(a*0.05))
        # > dispaly the final price after discount

userPrice = float(input('Total price of shopping'))
customer = input('You are student or not (yes or no )')

if customer == 'yes':
 discount = (userPrice-(userPrice*0.1))
 print(discount)

elif customer == 'no':
  discount = (userPrice-(userPrice*0.05))
  print(discount)

    # Task 04 : 
        # Wirte a simple banking system programm that :
        # Ask the user to choose one from the menu.
        # Deposite money (Add a float amount to tha initial balance )
        # withdraw money (Substract a float  amount from the initial balance)
        # Display (Display the balance)

Balance = int(input('Enter your balance'))

print ('Enter 1 for Deposit')
print ('Enter 2 for Withdraw')
print ('Enter 3 for Display')

menu = int(input('Choose any one'))
if menu == 1 :
 int(input('how much you want deposit in'))
 deposite = Balance + menu
 print("New Balance ",deposite)
elif menu == 2 :
 int(input('how much you want to withdraw'))
 withdraw = Balance - menu
 print("New Balance ",withdraw)

    # Task 05 : 
        # Write a profram to check that if the string is a palendrom 

palendrom = input('Enter Any word for check is palendrom')

isPalendrom = palendrom[::-1]

if palendrom == isPalendrom :
 print('Yes Its palendrom word')

    # Task 06 :
         #write a program that takes integers as input & categorize them into different lists as even and odd
integer1 = int(input('Enter Integers'))
integer2 = int(input('Enter Integers'))

listEven = []
listOdd = []

if integer1%2 == 0 and integer2%2 ==0 :
 listEven.append(integer1 , integer2)
 print('Its Even', listEven)

elif integer1%2 != 0 and integer2%2 !=0 :
 listOdd.append(integer1 , integer2)
 print('Its Even', listOdd)

    # Task 07 ; 
        # Write a program that : 
        # Takes a paragraph as input :
        # Count the total number of words in the paragraph
        # Count the number of spaces
        #Replace 'and' with &

para = input('Enter paragraph')










