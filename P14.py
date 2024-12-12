import datetime
class Employee:
    
    numofemp = 0
    raiseamount = 1.04
        
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.numofemp += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def applyraise(self):
        self.pay =int(self.pay * self.raiseamount)
        
    @classmethod
    def setraiseamount(cls, amount):
        cls.raiseamount = amount
        
    @classmethod
    def fromstring(cls,empstr):
        first, last, pay = empstr.split('-')
        return cls (first, last, pay)
    
    @staticmethod
    def isworkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True
    
emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

mydate = datetime.date(2024, 11, 12)

print (Employee.isworkday(mydate))

