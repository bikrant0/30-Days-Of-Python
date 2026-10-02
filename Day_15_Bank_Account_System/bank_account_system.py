# Bank Account System

class Bank:
        def __init__(self, first, last, branch, address):
            self.first = first
            self.last = last
            self.branch = branch, address
            self.email = first + last +'@'+ branch.lower() + 'com'

        def fullname(self):
             return '{} {}'.format(self.first, self.last)

class Customer(Bank):
    def __init__(self, first, last, branch, address):
        super().__init__(first, last, branch, address)


    raise_amount = 1.04

class Employee(Bank):

    raise_amt = 1.04

    def __init__(self, first, last, branch, address, pay):
        super().__init__(self,first, last, branch, address)
        self.pay = int(self.pay * 1.04)

class Manager(Employee):
    def __init__(self, first, last, branch, address, pay, employees= None):
          super().__init__(first, last, branch, address, pay)
          if employees is None:
                self.employees = []
          else:
               self.employees = employees 

    def add_emp(self, emp):
        if emp not in self.employees:
             self.employees.append(emp)

    def remove_emp(self, emp):
            if emp not in self.employees:
                 self.employees.remove(emp)
    
         
    def print_emps(self):
         for emp in self.employees:
              print('-->' , emp.fullname())


bank1 = Bank('Nepal' ,'Investment Bank', 'Kathmandu','Kathmandu')
bank2 = Bank('Standard Chartered', 'Bank', 'Baneshwor', 'Baneshwor')

customer1 = Customer('Hanuman', 'Chandra','Tinkune', 'Baneshwor')

mgr_1 = Manager('Sue', 'Smith', 'Lalitpur', 'Lalitpur', 60000, [bank1] )

print(bank1.fullname())
print(customer1.email)
