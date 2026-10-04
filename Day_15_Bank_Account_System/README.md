# Day 15: Bank Account System (OOP)

A modular, object-oriented command-line Bank Account System. It demonstrates class inheritance, method overriding, and proper data encapsulation. Built as part of the **30 Days of Python Challenge**.

## How to Run

1. Ensure Python is installed on your machine.
2. Run the script from your terminal:
   `python bank_account_system.py`
3. The script will automatically initialize sample data (Customers, Employees, Managers, and Accounts) and run a series of tests to demonstrate the system's features.

## Project Structure
Day_15_Bank_Account_System/
├── bank_account_system.py # Main application script with all classes
└── README.md # This file


## Features

- ✅ **Inheritance:** `Customer`, `Employee`, and `Manager` inherit core attributes (name, email) from a base `Person` class.
- ✅ **Specialized Accounts:** `SavingsAccount` and `CheckingAccount` inherit from `BankAccount` and add specific features (e.g., interest rates, overdraft limits).
- ✅ **Managerial Control:** Managers can add/remove employees and view their team's details.
- ✅ **Safe Transactions:** Deposit and withdraw methods use `try/except` blocks to prevent crashes from invalid user input.
- ✅ **Professional Structure:** Execution is guarded by `if __name__ == "__main__":` to prevent accidental execution on import.

## Daily Developer Log

### Day 15: Bank Account System

- **What I built:** A complete Object-Oriented Bank Account System featuring a hierarchy of People (Customers, Employees, Managers) and financial Accounts (Savings, Checking).
- **What broke / what confused me:** 
  - Initially trying to make `Customer` and `Employee` inherit directly from a `Bank` class, which created a confusing "is-a" vs "has-a" relationship.
  - Passing too many arguments to `super().__init__()` when the parent class didn't expect them.
  - Accidentally nesting the `Savings` class *inside* `BankAccount`, which prevented proper inheritance.
  - Placing the `if __name__ == "__main__":` execution block at the top of the file, causing `NameError`s because the classes weren't defined yet.
- **What I understand better now:** 
  - How to properly design an OOP hierarchy: separating the "Person" (who they are) from the "Account" (what they have).
  - How `super().__init__()` strictly requires matching the parent class's expected arguments.
  - The importance of the `if __name__ == "__main__":` guard and keeping execution logic at the very bottom of the file.
  - How to safely handle user input for financial transactions using `try/except ValueError`.
- **Time spent:** 2 hours
- [**DONE**] Committed to GitHub.