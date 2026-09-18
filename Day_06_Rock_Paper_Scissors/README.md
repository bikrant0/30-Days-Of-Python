# Day 6: Rock , Paper, Scissor

A small game: Rock, Paper, Scissor built as part of the **30 Days of Python Challenge**. This project generates random passwords of any length using letters, digits, and special characters.

## How to Run

1. Ensure Python is installed on your machine.
2. Run the script from your terminal:
   `python rock_paper_scissors.py`

## Daily Developer Log

### Day 6: Rock, Paper, Scissors

- **What I built:** An interactive game that takes user input (accepting both full words like "rock" and shorthand like "r"), generates a random computer choice, compares them to determine a win/loss/tie, and loops continuously until the user decides to quit.
- **What broke / what confused me:** I forgot that strings are case-sensitive and exact ("rock" does not equal "Rock!"). Logic traps where the game would declare a win even if the user lost, because I didn't check the computer's specific winning counter-move.
  - Accidentally used `break` on a tie, which ended the entire game instead of just skipping to the next round.
- **What I understand better now:** 
  - How to properly use the `in` and `not in` keywords to check if a value exists inside a tuple or list.
  - The critical difference between `=` (assignment) and `==` (comparison).
  - How to use `continue` to skip the rest of a loop iteration (perfect for handling invalid inputs or ties).
  - How to structure nested `if/elif/else` blocks to handle complex, multi-condition game logic.
  - How to force valid input using a `while` loop (for the "play again" prompt).
- **Time spent:** 75 mins
- [**DONE**] Committed to GitHub.

