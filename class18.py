#Recursion

# Define a recursive function to calculate the factorial of a number
def recur(i):
    if i == 0:
        return 1
    else:
        return i * recur(i-1)

recur(5)  

# Sum of Natural Numbers
def facsum(j):
    if j == 0:
        return 1
    else:
        return j + recur(j-1)
facsum(5)

# Develop a function to calculate the sum of values within a list using recursion
def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

sum_list([1, 2, 3, 4, 5])

# Develop a function to calculate n numbers of Fibonanci series using recursion
# n should be taken from user input 
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
print("Fibonacci series:", fibonacci(num_terms))