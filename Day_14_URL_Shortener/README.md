# Day 14 — URL Shortener

A CLI URL shortener that calls the TinyURL API to shorten a user-provided link. Built as part of the **30 Days of Python Challenge**.

## How to Run

1. Ensure Python and the `requests` library are installed (`pip install requests`).
2. Run the script from your terminal:
   `python url_shortener.py`
3. Enter a full URL (including `http://` or `https://`) when prompted.

## Daily Developer Log

### Day 14: URL Shortener (CLI)

- **What I built:** A CLI app that validates a user-entered URL, calls TinyURL's API via `requests.get()`, and prints the shortened link.
- **What broke / what confused me:**
  - I left a bare `try:` with no `except`, causing a `SyntaxError`.
  - Inverted the `startswith("http")` condition multiple times, alternately skipping the valid-URL case or the invalid-URL case.
  - Caught `ValueError` for a no-internet scenario, when the real exception was `requests.exceptions.ConnectionError` (wrapping a lower-level `urllib3` `NameResolutionError`).
  - Forgot to add an `else` branch for invalid URLs after restructuring the `if`, so bad input silently produced no output at all.
- **What I understand better now:**
  - Exception layering: catch at the level of the library you import directly (`requests`), not its internal dependencies (`urllib3`).
  - `.text` vs `.json()` — not every API returns JSON; check what the response actually is before parsing it.
  - The importance of testing every branch of a conditional, not just the one currently being debugged.
- **Time spent:** ~2 hours (across multiple debugging rounds)
- [**DONE**] Committed to GitHub.