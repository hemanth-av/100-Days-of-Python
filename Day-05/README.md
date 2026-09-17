# Day 05 - Password Generator

A command-line password generator that creates a secure, randomized password based on the user's preferred number of letters, symbols, and numbers.

## How It Works

1. User specifies how many letters, symbols, and numbers they want.
2. Random characters are picked from each category and added to a list.
3. The list is shuffled to mix all characters randomly.
4. The final password is assembled and displayed.

## Key Concepts Used

- **`random.choice()`:** Picks a random character from a list.
- **`random.shuffle()`:** Shuffles the password list to randomize character order.
- **`for` loops:** Iterates to build each section of the password.
- **Lists:** Stores letters, numbers, symbols, and the assembled password characters.
- **String Concatenation:** Joins the shuffled list into a final password string.
- **`f-strings`:** Formats the output message cleanly.