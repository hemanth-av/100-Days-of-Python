# Day 7 - Hangman Game

## How It Works
1. A random word is chosen from a word list
2. The word is displayed as underscores (`_`) representing each letter
3. Player guesses one letter at a time — correct guesses reveal the letter in position
4. Each wrong guess costs a life (6 lives total) and advances the hangman drawing
5. Game ends when the word is fully guessed (win) or all 6 lives are lost (lose)

## Key Concepts
- **while loops** — keeps the game running until win or lose condition is met
- **for loops** — iterates over each letter to build the display string
- **random.choice()** — picks a random word from the word list
- **Importing modules** — splits code across multiple files (`hangman_art.py`, `hangman_words.py`)
- **Lists** — tracks correctly guessed letters
- **String indexing** — checks and reveals letters at correct positions

## Files
| File | Description |
|------|-------------|
| `main.py` | Core game logic |
| `hangman_art.py` | ASCII art for hangman stages and logo |
| `hangman_words.py` | Word list for random selection |

## How to Run
```bash
python main.py
```