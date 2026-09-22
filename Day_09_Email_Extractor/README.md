# Day 9: Email Extractor

A command-line tool that reads a text file and extracts all valid email addresses using Regular Expressions (Regex). Built as part of the **30 Days of Python Challenge**.

## How to Run

1. Ensure Python is installed on your machine.
2. Create a text file (e.g., `data.txt`) with some text and hidden email addresses.
3. Run the script from your terminal:
   `python email_extractor.py`

## Daily Developer Log

### Day 9: Email Extractor

- **What I built:** A script that opens a text file, reads its contents, and uses the `re` (Regular Expression) module to find and extract all valid email addresses, printing them cleanly to the console.
- **What broke / what confused me:** 
  - Using `file.readlines()` instead of `file.read()`, which caused a `TypeError` because Regex expects a single string, not a list of strings.
  - Trying to loop over an integer (`for i in len(emails):`), which crashes Python.
  - Variable naming confusion between the list of emails and the count of emails.
  - Placing introductory print statements inside the `for` loop, causing them to repeat for every email found.
- **What I understand better now:** 
  - How to use the `re` module, specifically `re.findall(pattern, text)` to extract data based on a regex pattern.
  - The importance of using `file.read()` when you need the entire file as one continuous block of text.
  - How to properly iterate through a list of results using a `for` loop.

- **Time spent:** 1.5 hours
- [**DONE**] Committed to GitHub.