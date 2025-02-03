# Today Learned help() Metohd , LEGB rules ,
# Arguments Type (posiitonal Argument => arbitrary and keyword => kwarg) 
# Task 

# 01 : Write the program to count odd numbers using fun 

def oddNumber(findOdd):
    count =0
    for i in findOdd:
        if i%2 != 0:
            count+=1
    print(count)
odd = [1,2,3,4,5,6,7,8]
oddNumber(odd)

# 02 : write a program to count neg numbers using functions

def negNumber(findneg):
    count = 0
    for i in findneg:
        if i < 0:
            count += 1
    return count  
neg = [1, 2, -3, 4, -5, 6, -7, 8]
result = negNumber(neg) 
print(result) 

# 03 : write a program to sum the number taking multiple arguments

def sum_numbers(*args):
  total = 0
  for num in args:
    total += num
  return total


result1 = sum_numbers(1, 2, 3)
result2 = sum_numbers(10, 20, 30, 40, 50)

print(f"Sum of 1, 2, 3: {result1}")
print(f"Sum of 10, 20, 30, 40, 50: {result2}")

# 04 : Write a function to check is string provided by user is palindrom

palendrom = input('Enter Any word for check is palendrom')
def findPalindrom(checkPalendrom):

    isPalendrom = checkPalendrom[::-1]
    if checkPalendrom == isPalendrom :
        print('Yes Its palendrom word')

findPalindrom(palendrom)

# 05 : write a program to find out the number of vowels and count of each vowel in string provided

vowelList = input('Enter name for finding vowel')
def findvowel(vowel):
    count =0
    for i in vowel:
        if i == 'a' or i =='e' or  i =='i' or i =='o' or i =='u':
            print(f'vowel is {i}')
            count +=1
    print(f'Total vowel is{count}')
findvowel(vowelList)   