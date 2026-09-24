# Day 11: Dictionary Saver

A persistent command-line dictionary application that allows users to add words, look up definitions, and save their progress to a local JSON file. Built as part of the **30 Days of Python Challenge**.

## How to Run

1. Ensure Python is installed on your machine.
2. Run the script from your terminal:
   `python dictionary_saver.py`
3. Follow the on-screen menu to add words, search for definitions, or save and quit.
4. The data is automatically saved to `dictionary.json` and will be loaded the next time you run the app!

## Daily Developer Log

### Day 11: Dictionary Saver

- **What I built:** An interactive dictionary app that uses the `json` module to read and write data to a file. It features a continuous loop for adding/searching words, and safely handles cases where the save file doesn't exist yet.
- **What broke / what confused me:** 
  - The difference between using literal strings (`my_dict['word']`) and variables (`my_dict[user_word]`) when assigning dictionary keys.
  - Trying to save the file *after* using the `break` statement, which caused the save code to be skipped entirely.
  - Confusing `json.loads()` (which reads a string) with `json.load()` (which reads an open file object).
  - The flow of `try/except` blocks and realizing that if a file is missing, the variables inside the `try` block never get created.
- **What I understand better now:** 
  - How to use `json.dump()` to write Python dictionaries to a text file, and `json.load()` to read them back into memory.
  - How to use the `in` keyword to safely check if a key exists in a dictionary before trying to access it (preventing `KeyError` crashes).
  - How to use an `except FileNotFoundError:` block to initialize an empty dictionary `{}` so the program can start fresh if no save file exists.
  - The critical importance of saving data *before* executing a `break` or `return` statement.
- **Time spent:** 1 hours
- [**DONE**] Committed to GitHub.