# Day 12: Weather App (CLI)

A command-line currency converter that reads currency data values from an api or url and converts the amount user's inputted according to their choice. Built as part of the **30 Days of Python Challenge**.

## How to Run

1. Ensure Python is installed on your machine.
2. Make sure the internet is working fine. I didn't provide you API key.
3. Run the script from your terminal:
   `python currency_converter.py`
4. Enter the currency you have and targeted currency you want to convert the value.
5. The app will search the data and display the targetted currency.

## Daily Developer Log

### Day 12: Weather App (CLI)

- **What I built:** A CLI app that calls API, parses dictionary parsing and conversion of currency and amount.
- **What broke / what confused me:** 
  - Made mistake at API_KEY f-string issue.
  - Mixing up `==` vs `in` for looking up the data in dictionary.
  - The `except` block was not stopping execution that needed return.

- **What I understand better now:** 
  - Nested dictionary access
  - Difference between a Response object and its `.json().`
  - Why `try/except` need `return` to actually stop a function.
  - `in` for membership vs `==` for equality.
  
- **Time spent:** 2 hours
- [**DONE**] Committed to GitHub.