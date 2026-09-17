# Day 5: Password Generator

A secure, customizable password generator built as part of the **30 Days of Python Challenge**. This project generates random passwords of any length using letters, digits, and special characters.

## How to Run

1. Ensure Python is installed on your machine.
2. Run the script from your terminal:
   `python password_generator.py`

## Daily Developer Log

### Day 5: Password Generator

- **What I built:** This is a command-line tool that asks the user for a desired password length and generates a cryptographically random password using Python's `random` and `string` modules.
- **What broke / what confused me:** I tried to add intergers and strings together without conversion. I used pass as a variable name, which is a reserved Python keyword.
- **What I understand better now:** I learned that integers and strings cannot be added together without conversion. Using `"".join()` to combine a sequence of characters into a single string. I now know the Python entry point pattern. The string module has built-in constants like ascii_letters, digits, and punctuation that save you from typing out character pools manually.
- **Time spent:** 1 hour
- [**DONE**] Committed to GitHub.

