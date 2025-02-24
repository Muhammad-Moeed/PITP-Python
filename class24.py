# Multiple Inheritance & Multiline Inheritance
class X:
    def method(self):
        print('This is X')
class W:
    def method(self):
        print('This is W')
class A(W,X):     
    pass                                                                                                                           
    # def method(self):
    #     print('This is A')
class C(A,X):          
    pass                                                                                                                      
    # def method(self):
        # print('This is C')
        
# Answer = C()
# Answer.method()

# Task 1 
# create two parents class printer with attributes and methods and scanner with attributes and methods
# and a child class multifunctiondevice , that inherit from both
class Printer:
    def __init__(self, p):
        self.localprinter = p

    def printerHealth(self):
        return f"Printer health: {self.localprinter}"


class Scanner:
    def __init__(self, s):
        self.localscanner = s

    def scannerHealth(self):
        return f"Scanner health: {self.localscanner}"


class MultifunctionDevice(Printer, Scanner):
    def __init__(self, p, s):
        Printer.__init__(self, p)
        Scanner.__init__(self, s)

    def checkHealth(self):
        printer_health = self.printerHealth()  
        scanner_health = self.scannerHealth()  
        return printer_health, scanner_health


device = MultifunctionDevice('localPrinter', 'localScanner')
printer_health, scanner_health = device.checkHealth()
print(printer_health)
print(scanner_health)



