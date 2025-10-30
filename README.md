# 🐍 Reinforcement Learning Snake Agent

This repository implements a **Reinforcement Learning (RL) agent** that learns to play the classic *Snake Game* using the **Q-learning** algorithm.  
The environment, agent, and training loop were built entirely in **Python (PyGame + NumPy)**.

This is a **sanitized, educational version** of a Machine Learning I project at **Universidad Carlos III de Madrid (UC3M, 2024)**.

---

## 🎯 Objective
Train an RL agent that maximizes its score by learning an optimal movement policy through interaction with the game environment.

---

## 🧩 Methods Overview

### Environment (`snake_env.py`)
- Custom implementation of the Snake game using PyGame.
- State = (Direction, Food Direction, Collision Map).
- Total of **540 states** (4 × 9 × 15 combinations).
- Provides reward feedback, collision detection, and legal actions.

### Agent (`q_learning.py`)
- Implements **tabular Q-learning**.
- Parameters:
  - α (learning rate) = 0.5  
  - γ (discount factor) = 0.9  
  - ε (exploration rate) = 1.0 (decayed by 0.9999 per step)
- Stores and loads a Q-table from file (`q_table.txt`).

### Game Loop (`SnakeGame.py`)
- Coordinates training episodes and rendering.
- Can run in **training** or **playback** mode.
- Displays live visualization via PyGame when enabled.

---

## ⚙️ Reward Function

| Situation | Reward |
|------------|--------|
| Eats food | +10 |
| Gets closer to food | +1 |
| Moves away from food | -1 |
| Dies (collision) | -8 |

Reward shaping helps the agent gradually learn desirable behaviors.

---

## 🚀 How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/feligro/reinforcement-learning-snake-agent.git
cd reinforcement-learning-snake-agent/src
```

Licensed under the [MIT License](./LICENSE).
