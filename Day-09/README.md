# Day 9 - Silent Auction Program

## How It Works
1. Each bidder enters their name and bid amount
2. After each bid, the program asks if there are any other bidders (`yes` or `no`)
3. If any other input is entered, it prompts again with an error message
4. Once all bids are in, the program finds and announces the highest bidder as the winner

## Key Concepts
- **Dictionaries** — stores each bidder's name and bid as key-value pairs
- **Functions** — `find_highest_bidder()` loops through the dictionary to find the winner
- **while loops** — keeps bidding going and validates user input
- **Input validation** — rejects anything other than `yes` or `no`
- **Importing modules** — uses `art.py` for the logo display

## How to Run
```bash
python main.py
```