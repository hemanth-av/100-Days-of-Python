# Day 03 - Treasure Island 🪙

A text-based adventure game where the player navigates through a series of choices to find hidden treasure. One wrong move and it's Game Over!

## How It Works

1. The player starts at a crossroad and must choose to go `left` or `right`.
2. If they go left, they reach a lake and must choose to `wait` for a boat or `swim`.
3. If they wait, they arrive at a house with 3 doors: `red`, `yellow`, or `blue`.
4. Only one correct path leads to the treasure — all others end the game.

## Game Map

```
Crossroad → left → Lake → wait → 3 Doors → yellow → 🏆 You Win!
                               → red    → 🔥 Game Over
                               → blue   → 🐉 Game Over
                        → swim  → 🐟 Game Over
          → right → 🕳️  Game Over
```

## Key Concepts Used

- **`if / elif / else` statements:** Controls the branching story logic based on player input.
- **Nested Conditionals:** Each correct choice unlocks the next decision layer.
- **`input()` function:** Captures the player's choices at each stage.
- **`.lower()`:** Normalizes input so `Left`, `LEFT`, and `left` all work the same.
- **Raw String (`r'''...'''`):** Displays the ASCII art map without escape character conflicts.
- **`print()` function:** Outputs the story narrative, ASCII art, and game results.
