# Day 06 - Reeborg's World Maze Solver

A Python solution for navigating Reeborg through a maze using the **right-hand rule** algorithm. This project was built and run on the [Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json) online platform — no local setup required.

> ⚠️ This code runs exclusively on the Reeborg's World website. It uses built-in functions (`move()`, `turn_left()`, `at_goal()`, `right_is_clear()`, `front_is_clear()`) provided by the platform.

## How It Works

The maze is solved using the **right-hand rule**:

1. If the path to the **right is clear** → turn right and move forward.
2. Else if the path **ahead is clear** → move forward.
3. Else → turn left (to find a new direction).
4. Repeat until Reeborg reaches the goal.

## How to Run

1. Open [Reeborg's World Maze](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)
2. Copy the code from `main.py`
3. Paste it into the code editor on the website
4. Click **Run** to watch Reeborg solve the maze

## Key Concepts Used

- **Functions:** `turn_right()` is defined by combining three `turn_left()` calls since the platform only provides left turns.
- **`while` loop:** Keeps Reeborg moving until the goal is reached.
- **`if / elif / else`:** Implements the right-hand rule decision logic.
- **Built-in Platform Functions:** `move()`, `turn_left()`, `at_goal()`, `right_is_clear()`, `front_is_clear()`.
