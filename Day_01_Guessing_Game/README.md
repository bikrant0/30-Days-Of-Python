# Day 1: Number Guessing Game

A console-based number guessing game built using pure Python. This project features user input validation, dynamic random number generation, and a continuous main game loop.

## How to Run

1. Ensure Python is installed on your machine.
2. Run the script from your terminal:
   `python guessing_game.py`

## Daily Developer Log

### Day 1 — Number Guessing Game

- **What I built:** A replayable CLI number guessing game using `random` and nested `while` loops.
- **What broke / what confused me:** I initially struggled with infinite loops and comparing text inputs to mathematical integers. I also had a bug where typing a lowercase "n" failed to exit the game.
- **What I understand better now:** I understand how to wrap text inputs in `int()` to prevent math errors, how to nest a game loop inside a master `while` loop, and how to use `.upper()` to handle case-sensitive inputs.
- **Time spent:** 45 minutes
- [**DONE**] Committed to GitHub.