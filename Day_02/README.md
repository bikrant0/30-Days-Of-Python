# Day 2: Basic Calculator

A simple command-line calculator built as part of the **30 Days of Python Challenge**. This project demonstrates fundamental Python programming concepts including functions, loops, conditionals and error handling.

## How to Run

1. Ensure Python is installed on your machine.
2. Run the script from your terminal:
   `python basic_calculator.py`

## Daily Developer Log

### Day 1 — Number Guessing Game

- **What I built:** A basic arithmetic calculator with input validation, error handling and nested `while` loops.
- **What broke / what confused me:** I used C-style OR (||) inside a string instead of Python's or keyword. The while status == "y" or "Y": logic trap that created an accidental inifite loop. I messed up the error handling by putting the math operations inside the `try` block. O struggled with print formatting (mixing f-strings with commas and trailing variables.)
- **What I understand better now:** Functions are defined once and called with specific arguments. F-strings can evaluate math directly inside curly braces which makes codes more readable. Python uses English word `or` for OR conditions, not ||. I now know `try` and `except` to catch `ValueError` without breaking the app and to isolate `try` block.
- **Time spent:** 50 minutes
- [**DONE**] Committed to GitHub.