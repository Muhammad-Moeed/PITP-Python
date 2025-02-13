# File Handling 
f = open('class21.py','r') # Relative file open 
# print(f.read())
print(f.read(1))
print(f.read(2))
# print(f.seek(3))
print(f.readlines()[2])

import os
os.remove('abc.py')
f1 = open('C:/Users/Chemical/Desktop/hamza.py','a') # Absolute file open 
print(f1.write(''))
# print(f1.write())0