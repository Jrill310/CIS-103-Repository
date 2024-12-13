#Program number 15
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
        
        
class Dev(Employee):
    
    raiseamount = 1.10
    
    def __init__(self, first, last, pay, proglang):
        super().__init__(first, last, pay)
        self.proglang = proglang
        
class Man(Employee):
    
    raiseamount = 1.4
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.Employees = []
        else:
            self.employees = employees
            
    def addemp(self,Employee):
        if Employee not in self.employees:
            self.employees.append(Employee)
            
    def subemp(self,Employee):
        if Employee in self.employees:
            self.employees.remove(Employee)
        
    def printemp(self):
         for Employee in self.employees:
             print ('-->',Employee.fullname())
        
        
        
dev1 = Dev('Corey', 'Schafer', 50000, 'Python')
dev2 = Dev('Test', 'User', 60000, 'Java')

mgr1 = Man ('Sue', 'Smith', 90000, [dev1])

#print(isinstance(mgr1,Dev))
#print(issubclass(Man,Dev))

#print (mgr1.email)

mgr1.addemp (dev2)
mgr1.printemp()
#mgr1.subemp(dev1)

#mgr1.printemp()


#print (dev1.email)
#print (dev1.proglang)

#print(dev1.pay)
#dev1.applyraise()
#print(dev1.pay)


