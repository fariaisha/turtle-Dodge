# # 🐢 Ultimate Turtle Dodge

A fast-paced, classic arcade-style dodging game built entirely using Python's native **Turtle Graphics** library. Control a nimble green turtle, dodge falling red meteors, level up, and chase your own high score!

---

## 🎮 Features

- **Start Menu & Game Over Screen:** Clean, interactive text-based overlay states that seamlessly transition between phases with the spacebar.
- **Dynamic Difficulty Scaling:** Every 10 points scored advances your **Level**. As the level increases, obstacles drop faster and spawn much more frequently.
- **Persistent High Scores:** Saves your highest score locally to a text file (`highscore.txt`). The game remembers your best score even after closing it!
- **Smooth Rendering:** Optimized with manual `tracer` double-buffering updates to eliminate screen flickering common in basic Turtle games.

---

## 🛠️ Prerequisites

The game runs entirely on Python's built-in libraries. No complex third-party installations (like Pygame) are required!

- **Python 3.x** installed on your system.

---

## 🚀 How to Install and Run

1. **Clone the Repository:**
   ```bash
   git clone https://github.com
   cd ultimate-turtle-dodge
   ```

2. **Run the Script:**
   Execute the code using your terminal or command prompt:
   ```bash
   python turtle_game.py
   ```

---

## 🕹️ Controls


| Key | Action |
| :--- | :--- |
| **`SPACEBAR`** | Start the game / Play again after Game Over |
| **`LEFT ARROW`** | Move the turtle to the left |
| **`RIGHT ARROW`** | Move the turtle to the right |

---

## 📂 Project Structure

```text
ultimate-turtle-dodge/
│
├── turtle_game.py    # The main game executable source code
├── highscore.txt     # Generated automatically to keep your high score
└── README.md         # Project documentation (This file)
```

---


