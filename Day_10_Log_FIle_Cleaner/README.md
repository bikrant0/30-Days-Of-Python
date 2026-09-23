# Day 10: Log File Cleaner

A command-line utility that reads a messy log file, filters out specific unwanted entries (like `[DEBUG]`) using Regular Expressions, and writes the clean data to a new file. Built as part of the **30 Days of Python Challenge**.

## How to Run

1. Ensure Python is installed on your machine.
2. Create a sample messy log file named `log.txt` with various `[INFO]`, `[WARNING]`, and `[DEBUG]` entries.
3. Run the script from your terminal:
   `python log_file_cleaner.py`
4. Check the newly generated `clean_log.txt` file to see the filtered results.

## Daily Developer Log

### Day 10: Log File Cleaner

- **What I built:** A file processing script that reads a text file line-by-line, uses Regex to identify specific patterns (like `[DEBUG]`), and writes only the non-matching lines to a brand new output file.
- **What broke / what confused me:** 
  - The order of operations when opening two files at once.
  - Accidentally using the original filename in the `"w"` (write) mode, which instantly erased my original messy log file before I could read it!
  - Understanding how Regex square brackets `[ ]` work (they mean "pick one character from a menu", not "group these words together").
  - Remembering to escape literal brackets in Regex using backslashes (`\[DEBUG\]`).
  - Forgetting that `re.search()` looks *inside* a string, whereas `==` checks for an *exact* match.
- **What I understand better now:** 
  - How to use nested `with open()` blocks to safely read from one file and write to another simultaneously.
  - How to use `re.search(pattern, text)` combined with the `not` keyword to filter out unwanted data.
  - The importance of using different variable names for input files (`messy_file`) and output files (`clean_file`) to prevent variable collision.
  - How to process massive files efficiently by iterating line-by-line (`for line in file:`) instead of loading the whole file into memory.
- **Time spent:** 1.5 hours
- [**DONE**] Committed to GitHub.