# Day 8: File Word Counter

A simple command-line tool that reads a text file and counts the total number of words using file I/O and string splitting. Built as part of the **30 Days of Python Challenge**.

## How to Run

1. Ensure Python is installed on your machine.
2. Run the script from your terminal:
   `python file_word_counter.py`
3. Enter a filename or press Enter to use the auto-generated `sample.txt`.

## Daily Developer Log

### Day 8: File Word Counter

- **What I built:** A tool that opens a text file, reads its contents, splits the text into individual words, and counts them. It auto-creates a sample file so it works immediately and handles missing files gracefully.
- **What broke / what confused me:** Understanding how `open()` works with the `with` keyword and why it is safer than manually opening and closing files. Learning that `.split()` without arguments splits on all whitespace (spaces, tabs, newlines) automatically.
- **What I understand better now:** How to use `open(filename, "r")` to read files and `open(filename, "w")` to write files. How the `with` statement automatically closes the file even if an error occurs. How `.split()` breaks a string into a list of words and how `len()` counts them. How to handle `FileNotFoundError` with try/except.
- **Time spent:** 15 minutes
- [**DONE**] Committed to GitHub.