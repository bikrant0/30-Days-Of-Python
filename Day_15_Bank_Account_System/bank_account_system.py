# Bank Account System


class Person:
        def __init__(self, first, last):
            self.first = first
            self.last = last
            self.email = first.lower() + '.' + last.lower() + '@company.com'

        def fullname(self):
             return '{} {}'.format(self.first, self.last)
             

class Customer(Person):
    def __init__(self,first,last, account):
        super().__init__(first, last)
        self.account= int(account)

class Employee(Person):
    def __init__(self,first, last, account, pay, position):
        super().__init__(first,last)
        self.account = int(account)
        self.pay = float(pay)
        self.position = position
        self.raise_amt = 1.04




class Manager(Employee):
    def __init__(self,first,last, account, pay, position, employees=None):
        super().__init__(first,last, account, pay , position)
        self.employees = employees if employees is not None else []

    def add_emp(self, emp):
        if emp not in self.employees:
             self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
         
    def print_emps(self):
         for emp in self.employees:
              print('-->' , emp.fullname())

    def view_details(self):
         for emp in self.employees:
              print('Fullname', emp.fullname())
              print('Position', emp.position)
              print('Pay', emp.pay)

            

class BankAccount():
    def __init__(self, first, last, account, balance = 0.0):
        self.first = first
        self.last = last
        self.account = account
        self.balance = float(balance)
        
        
    def deposit(self):
        depo = input("Enter the amount/balance you want to deposit: ")
        try:
            amount = float(depo)
            self.balance += amount
            print(f"You have successfully deposited {amount}. Your current balance is {self.balance}.")
        except ValueError:
                print("Please enter only numbers. not strings.")


    def withdraw(self):
            withd = input("Enter the amount/balance you want to withdraw: ")
            try:
                if withd == float(withd):
                    self.balance = self.balance - float(withd) 
                    print(f"Successfully withdrawn {withd}. Current balance: {self.balance}")
            except ValueError:
                print("Please enter only numbers. not strings.")
                 


    def statement(self):
        return f"Account: {self.account} | Balance: {self.balance}"
    
class SavingsAccount(BankAccount):
    def __init__(self,first, last, account, balance = 0.0, interest_rate = 1.05):
        super().__init__(first, last, account, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance *= self.interest_rate
        print(f"Interest applied! New Balance: {self.balance}")

class CheckingAccount(BankAccount):
    def __init__(self, first, last, account, balance=0.0, overdraft_limit=0.0):
        super().__init__(first, last, account, balance)
        self.overdraft_limit = overdraft_limit



def bank_account_system():
    print("----Initializing Bank System ---\n")

    # 1. Data Samples
    customer1 = Customer('Ram', 'Sharma', 1001)
    emp1 = Employee('John', 'Doe', 2001, 50000, 'Teller')
    emp2 = Employee('Jane', 'Smith', 2002, 55000, 'Loan Officer')
    mgr_1 = Manager('Sue', 'Anderson', 3001, 80000, 'Branch Manager', [emp1, emp2])

    # 2. Sample Accounts
    acc1 = SavingsAccount('Ram', 'Sharma', 1001, 1000.0)

    # 3. Test Person/Manager Features
    print("Manager:", mgr_1.fullname())
    print("Customer Email:", customer1.email)
    print("\nManager's Team:")
    mgr_1.view_details()

    # 4. Test Account Features
    print("\n--- Account Testing ---")
    print("Initial:", acc1.statement())
    acc1.apply_interest()
    print("After Interest:", acc1.statement())
    
    print("\n--- System Ready! ---")

if __name__ == "__main__":
    bank_account_system()