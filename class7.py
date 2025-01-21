# Today Covered Nested Objectd and Get ,
# Update and Delete value from Nested Object

# Task 01 :
# Create a library managment system using a nested dictnary where :
# 1 : Each book has a uniqque ID as a key ,
# 2 : Each book contains details like title , another and availablity

# write a program :
# > to add a new book
# > borrrow book(change its availablity to false)
# > return a book (change its availbility to true)

lms = {
    1: {
        'title': 'English',
        'description': 'Whether reading ',
        'available': True

    },
    2: {
        'title': 'Math',
        'description': 'Whether reading the short or long ',
        'available': True

    },
    2: {
        'title': 'Scienece',
        'description': 'Whether reading the short ',
        'available': True

    }
}
lms.update({
    4: {
        'title': 'Urdu',
        'description': 'Whether reading /',
        'available': True

    }
})

borrowBook = lms[1]['available'] = False
print(borrowBook)
print(lms)

# Task 02 :
# you have dictonary of students and their grades in different subjects , find
# the avg of each students marks individually and then add them dictonary with key
# 'avg_marks' .

students = {
    "1": {
        'math': 100,
        'english': 80
    },
    "2": {
        'math': 50,
        'english': 70
    },
    "3": {
        'math': 80,
        'english': 100
    }
}

students1_math = students['1']['math']
students1_english = students['1']['english']
students2_math = students['2']['math']
students2_english = students['2']['english']
students3_math = students['3']['math']
students3_english = students['3']['english']

student1Avg = (students1_english + students1_math) / 2
student2Avg = (students2_english + students2_math) / 2
student3Avg = (students3_english + students3_math) / 2

students["1"]['avg'] = student1Avg
students["2"]['avg'] = student2Avg
students["3"]['avg'] = student3Avg

if student1Avg >= student2Avg and student1Avg >= student3Avg:
    print("Student1 Avg is Higest ", student1Avg)
elif student2Avg >= student1Avg and student2Avg >= student3Avg:
    print("Student2 Avg is heigest ", student2Avg)
elif student3Avg >= student1Avg and student3Avg >= student2Avg:
    print("Student3 Avg is Heigest ", student3Avg)
else:
    print("No Avg Heigh Student ")

# Task 03 :
# write a program to :
# 01 : add a new employe id 103
# 02 : update the sallery of the employee with id 102
# 03 : print department of the employee with id 101

employee = {
    '101': {
        'Name': 'ali',
        'Dept': 'IT',
        'Sallery': '2lac'
    },
    '102': {
        'Name': 'Anus',
        'Dept': 'IT',
        'Sallery': '4lac'
    }
}

employee.update({
    '103': {
        'Name': 'murtaza',
        'Dept': 'Machenical',
        'Sallery': '8lac'
    }
}
)

employee['102']['Sallery'] = ['10lac']
print("Dept of 101 : ", employee['101']['Dept'])
print(employee)


# Task 3 : 
# Following dictnoray shows weakly sales of a smartphones shopkeeper
# Calaclulate total number of phones sales in weaks 
# Calculate of samsung and nokia 

sales = {
    'Monday': {'Samsung': 5, 'Nokia': 3, 'Apple': 2},
    'Tuesday': {'Samsung': 7, 'Nokia': 4, 'Apple': 3},
    'Wednesday': {'Samsung': 6, 'Nokia': 2, 'Apple': 1},
    'Thursday': {'Samsung': 8, 'Nokia': 3, 'Apple': 4},
    'Friday': {'Samsung': 4, 'Nokia': 5, 'Apple': 3},
    'Saturday': {'Samsung': 10, 'Nokia': 6, 'Apple': 2},
    'Sunday': {'Samsung': 9, 'Nokia': 4, 'Apple': 3}
}

# Calculate total sales for the week
total_sales = sum(sum(day.values()) for day in sales.values())

# Calculate total sales for Samsung and Nokia
samsung_sales = sum(day.get('Samsung', 0) for day in sales.values())
nokia_sales = sum(day.get('Nokia', 0) for day in sales.values())

# Display the results
print(f"Total phone sales in the week: {total_sales}")
print(f"Total Samsung sales in the week: {samsung_sales}")
print(f"Total Nokia sales in the week: {nokia_sales}")
