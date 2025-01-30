# While loop Problems Solving Question 

# Q9:Write a program that:
# * Accepts a list of integers from the user.
# * Use a loop to find and print all the duplicate
# elements in the list.
# * Print the duplicate number & its count.


# Q10: Write a program that:
# * Accepts a number n as input.
# * Uses a loop to generate the first n numbers 
# in the fibonacci sequence.
# * Prints the sequence as a list.
# Example Output:
# Enter a number for Fibonacci Seq: 5
# Fibonacci Seq: [0,1,1,2,3]

# Q11: Write a program that:
# * Accepts a number n from the user.
# * Uses a loop to print the multiplicaton
# table for n upto 10.
# * Example Output:
# Enter the Number: 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15

# Q12: Write a program that:
# * Uses a dictionary to store expense categories 
# and amounts.
# *Allows the user to:
# 	1. Add expenses to a category (loop untill
# 	the user types 'stop')
# 	2. View all expenses by category.
# 	3. Calculate the total amount spent.
# * Exit the loop when the user is done.

    # Task 1 
        # Write a program that
        # Use a loop to find and print all the dublicate elements in the list
        # Print the dubilicate number & its count

integer=[]
a=int(input('How many number you want to add in the list'))
for i in range(a):
    b=int(input('Enter any num :'))
    integer.append(b)
    
dubilicate =[]
single=[]
for j in integer:
    count=0
    if j not in single:
        single.append(j)
    else:
        dubilicate.append(j)
        # count=+1
        print(f'{j} is the dubilicate number with count {integer.count(j)}')
      
        
        
    
    