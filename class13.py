# Class 13 
# While loop and signle lne statement in while loop

    # Task 1 : 
    # Find the sum of 10 natural number 
natural = 1
while natural<=10:
    print(natural)
    natural +=1


    # Task 2 :
    # find the factorial of 8
fact = 1
num = 1 

while fact<=8 :
    num*= fact
    print(num)
    fact+=1

    # Task 3 :
    # print reverce counting 1-10
reverce = 10
while reverce >=1:
    print(reverce)
    reverce-=1

    # task 4 :
    # write a program to find out the prime number in a range of 50 while loop

i =2

while i<=50:
        for j in range(2,i):
            if i%j == 0:
                print(i,' its not a prime number')
                break
        else:
            print(i,' Its  a prime number')
        i+=1
        
# Task 4 : 
    # write a program to guess the number 1 t o9 
    # 1 : Take input from user

import random
num=random.randint(1,9)
guess = int((input("Enter Number")))

while num == guess:
    print("You won the toss")
else:
    print("You Loss the toss")