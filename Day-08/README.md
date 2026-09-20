# Day 08 - Caesar Cipher 🔐

A command-line encryption and decryption tool based on the classic **Caesar Cipher** algorithm. The user can encode or decode any message by shifting letters a chosen number of positions through the alphabet.

## How It Works

1. User chooses to `encode` (encrypt) or `decode` (decrypt).
2. User enters the message and a shift number.
3. Each letter in the message is shifted forward (encode) or backward (decode) by the shift amount.
4. Non-alphabet characters (spaces, numbers, symbols) are kept unchanged.
5. The result is displayed and the user can run it again or exit.

## Example

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
5
Here is the encoded result: mjqqt
```

## Project Structure

```
Day-08/
├── main.py      # Main program logic
├── art.py       # ASCII art logo
└── README.md
```

## Key Concepts Used

- **Functions:** `caesar()` handles both encoding and decoding in a single reusable function.
- **`while` loop:** Keeps the program running until the user chooses to exit.
- **Modulo operator (`%`):** Wraps the shift around the alphabet to handle overflow (e.g. shift past `z`).
- **`list.index()`:** Finds the position of each letter in the alphabet list.
- **Negative Shift:** Decoding is handled by multiplying the shift by `-1`.
- **Modules:** `art.py` is imported to display the ASCII logo.
- **`.lower()`:** Normalizes all input to lowercase for consistent processing.
