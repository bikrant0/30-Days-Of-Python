# Day 12: Weather App (CLI)

A command-line weather application that reads historical weather data from a local JSON file and displays formatted weather metrics for a specific city. Built as part of the **30 Days of Python Challenge**.

## How to Run

1. Ensure Python is installed on your machine.
2. Make sure the `history_bulk.json` file is in the same directory as the script.
3. Run the script from your terminal:
   `python weather_app.py`
4. Enter a city name when prompted (e.g., `London`). **Note** The history_bulk.json contains only London city.
5. The app will search the data and display the first matching weather record!

## Daily Developer Log

### Day 12: Weather App (CLI)

- **What I built:** A CLI app that parses a bulk JSON file containing historical weather data. It takes user input for a city name, loops through the list of dictionaries to find a match, extracts nested dictionary values (temperature, clouds, date), and formats them cleanly using f-strings.
- **What broke / what confused me:** 
  - Trying to use `.keys()` on a list, and forgetting that I needed to look at the dictionaries *inside* the list.
  - The "else trap" inside a `for` loop (accidentally printing "not found" on every single iteration instead of just once at the end).
  - F-string syntax errors: mixing up quotes (using double quotes inside double quotes) and forgetting that the `f` prefix needs to be on every line of a multi-line string.
  - Trying to access nested dictionary keys incorrectly by grouping them together (e.g., `item["main"]["temp", item["clouds"]]`).
- **What I understand better now:** 
  - How to inspect raw JSON data by printing the first index (`data[0]`) to understand the "shape" and exact key names of nested dictionaries.
  - How to properly chain dictionary keys to access deeply nested data (e.g., `item['main']['temp']` and `item['clouds']['all']`).
  - How to use a boolean "flag" variable (like `found = False`) combined with a `break` statement to safely handle search logic and stop a loop early.
- **Time spent:** 2 hours
- [**DONE**] Committed to GitHub.