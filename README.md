# Coding Challenge Hui

This little coding is project is to spots where a smaller word (subtext) appears in a longer sentence (text). It doesn’t care about capital or lowercase letters and it will tells you the starting positions where matches are found.

## What it does
Ignores case (e.g. "Peter" and "peter" are treated the same)
Finds all matches and shows where each one starts (positions are 1-based)
If nothing matches, it says <Sorry nothing matched>
Doesn’t use built-in helpers like .find() or .lower()

## Files
- `string_search.py` – The main logic
- `main.py` – Lets you type text and subtext to search
- `test_string_search.py` – Runs tests to make sure the code works

## How to run
### Run it locally:
python3 main.py

### Run the test:
python3 test_string_search.py
