# Day 02 - Tip Calculator

A simple command-line tip calculator that takes the total bill, desired tip percentage, and number of people, then calculates how much each person should pay.

## How It Works

1. User enters the total bill amount.
2. User selects a tip percentage (10, 12, or 15%).
3. User enters the number of people splitting the bill.
4. The program calculates and displays the amount each person owes.

## Key Concepts Used

- **`float()`:** Converts the bill input to a decimal number to handle cents.
- **`int()`:** Converts tip percentage and number of people to whole numbers.
- **`input()` function:** Collects user input from the console.
- **Arithmetic Operators:** Uses `*` and `/` to calculate the tip and split the bill.
- **Variables:** Stores intermediate values (`bill`, `tip`, `people`, `total_bill`, `final_bill`).
- **New Line Escape Character (`\n`):** Formats prompts neatly on a fresh line.
