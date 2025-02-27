# Decorators 
# ===========
# A decorator is a function that takes another function as an argument and extends the behavior of the latter
# function without permanently modifying it.

# ****************Decorator import time*******************
import time
def decor(f):
    def wrapper():
        Date =time.localtime().tm_mday
        Month = time.localtime().tm_mon
        Year = time.localtime().tm_year
        startTime = time.time()
        endTime = time.time()
        print(f'Today Date : {Date}-{Month}-{Year}')
        print(f'Start Time : {startTime}')
        f()
        print(f'End Time : {endTime}')
    return wrapper
@decor
def func():
    print('Hello Moeed Qadri')
    input()
    
func()

# *******************Create Decorators*************
def myDecorator(func):
    def myWrapper():
        print('Wrapper before func execution')
        func()
        print('Wrappper after func execution')
    return myWrapper 
                    
@myDecorator
def myFunc():
    print('Decorated')        
myFunc()


