# Day 7: Countdown Timer

A simple command-line countdown timer built as part of the **30 Days of Python Challenge**. This project allows the user to set a timer in minutes, counts down second-by-second, and handles invalid inputs gracefully.

## How to Run

1. Ensure Python is installed on your machine.
2. Run the script from your terminal:
   `python countdown_timer.py`

## Daily Developer Log

### Day 7: Countdown Timer

- **What I built:** An interactive timer that asks the user for a duration in minutes, converts it to seconds, and visually counts down second-by-second until the time is up. It includes input validation to prevent crashes and loops to allow multiple uses.
- **What broke / what confused me:** 
  - Asking the user for "minutes" but passing that raw number directly into `time.sleep()`, which only accepts seconds.
  - Using `time.sleep(total_time)` which just freezes the screen instead of actually counting down visually.
  - Forgetting to validate the input, causing the program to crash with a `ValueError` if the user typed a letter instead of a number.
  - Adding unnecessary `else: continue` statements at the end of the main loop.
- **What I understand better now:** 
  - How to use the `time` module, specifically `time.sleep(1)` to pause execution for exactly one second.
  - How to build a `while` loop that acts as a countdown by checking a condition (`> 0`) and decrementing a variable (`-= 1`).
  - How to combine a `while True` loop with a `try/except ValueError` block to force the user to enter valid, positive numbers.
  - That if a `while True` loop reaches the end of its block without hitting a `break`, it automatically restarts from the top.
- **Time spent:** 1 hour
- [**DONE**] Committed to GitHub.