
# String Methods
string = 'is string'

print(string.upper())
print(string.lower())
print(string.find('is'))
print(string.split())
print(string.count('is'))
print(string.replace('is', 'of'))
print(string.startswith('i'))
print(string.endswith('u'))

# List 
list= ['banana','apple','mango','fruits','','']

# Access List item and slice
update = list[0] = 'strawberry'
updateLast = list[5]= 'grapes'
print(updateLast)
print(list)
slice = list[1::2]
print(slice)

# Add List Item
list.insert(2,'abbple')
print(list)

#add Item in last
list.append('last')
print(list)

# Extand and Combined the list 
extend = ['extand','list']
list.extend(extend)
print(list)

#Remvoe Last Item
list.pop()
print(list)

#Remove Any Item From List
list.remove('extand')
print(list)

# Task1
stepSize = ['a', 'A', 1, 2, 'b', 'B', 2, 3, 'c', 'C', 3, 4, 'd', 'D']

alphabets1 = stepSize[0]
alphabets2 = stepSize[1]
alphabets3 =stepSize[4]
alphabets4 =stepSize[5]
alphabets5 = stepSize[8]
alphabets6 =stepSize[9] 
alphabets7 =stepSize[12]
alphabets8 =stepSize[13] 
print(alphabets1 + alphabets2 + alphabets3 + alphabets4 + alphabets5 + alphabets5 + alphabets6 + alphabets7 + alphabets8)


# Task2
var = 'computersoftwareengineering'
fos = var[10:7:-1]
print(fos)

neeraw = var[17:11:-1]
print(neeraw)

ringofwar = var[23::] +''+ var[9:16-1]
print(ringofwar)

puter = var[3:8]
print(puter)


