
![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.5.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Complete-success.svg)
```markdown
# 🎮 Tic-Tac-Toe AI with Minimax Algorithm

An intelligent Tic-Tac-Toe game implementation using the Minimax algorithm to create an unbeatable AI opponent. This project demonstrates adversarial search algorithms and optimal game-playing strategies.

## 🎯 Features

- **Unbeatable AI**: Implements the Minimax algorithm for perfect play
- **Interactive GUI**: Built with Pygame for a smooth gaming experience
- **Optimal Strategy**: AI never loses - best outcome is a draw
- **Clean Code**: Well-documented, follows best practices
- **Player Choice**: Play as X or O against the AI

## 🚀 Technologies

- **Python 3.12+**
- **Pygame**: For graphical interface
- **Minimax Algorithm**: Game tree search with recursive evaluation

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/devakowakou/tictactoe.git
cd tictactoe

# Install dependencies
pip install -r requirements.txt
```

## 🎮 Usage

```bash
# Run the game
python runner.py
```

Choose to play as X or O, then try to beat the AI! (Spoiler: you can't 😉)

## 🧠 How It Works

The AI uses the **Minimax algorithm** to evaluate all possible game states:

1. **Max Player (X)**: Tries to maximize the score (+1 for win)
2. **Min Player (O)**: Tries to minimize the score (-1 for win)
3. **Recursive Evaluation**: Explores the complete game tree
4. **Optimal Decision**: Chooses the move leading to the best outcome

### Algorithm Complexity
- **Time Complexity**: O(b^d) where b ≈ 9 and d ≈ 9 (max depth)
- **Space Complexity**: O(d) for recursion stack
- **Optimizations**: Early termination when winning move found

## 📁 Project Structure

```
tictactoe-minimax/
├── tictactoe.py          # Game logic and AI implementation
├── runner.py             # Pygame GUI
├── requirements.txt      # Dependencies
├── OpenSans-Regular.ttf  # Font file
└── README.md            # This file
```

## 🔧 Implementation Details

### Core Functions

- `player(board)`: Determines whose turn it is
- `actions(board)`: Returns all possible moves
- `result(board, action)`: Applies a move to the board
- `winner(board)`: Checks for a winner
- `terminal(board)`: Checks if game is over
- `utility(board)`: Returns the game score
- `minimax(board)`: Returns the optimal move

### Key Algorithms

```python
def minimax(board):
    """Returns optimal action using Minimax"""
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        _, best_action = max_value(board)
    else:
        _, best_action = min_value(board)
    
    return best_action
```

## 🎓 Learning Outcomes

- Understanding adversarial search algorithms
- Implementing game tree traversal
- Recursive problem-solving
- Optimal decision-making in zero-sum games
- Python best practices and clean code

## 🧪 Testing

The AI plays optimally, meaning:
- ✅ Never loses
- ✅ Always wins if opponent makes a mistake
- ✅ Forces a draw against perfect play

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add alpha-beta pruning for optimization
- Implement different difficulty levels
- Add game statistics tracking
- Improve the UI/UX

## 📝 License

This project is part of CS50's Introduction to Artificial Intelligence with Python course.

## 👨‍💻 Author

**Your Name**
- GitHub: [@devakowakou](https://github.com/devakowakou)
- Project: [CS50 AI - Week 0](https://cs50.harvard.edu/ai/)

## 🙏 Acknowledgments

- Harvard's CS50 AI course
- Minimax algorithm theory
- Pygame community

---

