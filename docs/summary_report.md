# Reinforcement Learning Agent for the Snake Game  
*Summary Report – Machine Learning I (UC3M)*  

**Repository Maintainer:** Felipe Grima Rodríguez  
**Collaborator:** Pedro Javier López Dondarza  
**Original Code Author (Anonymized):** J.L.P.  

> **Privacy note:**  
> The original course assignment contained personal identifiers and is therefore **not included**.  
> This document summarizes an anonymized and portfolio-safe version of the project, acknowledging  
> the original author and the academic context (Machine Learning I – Universidad Carlos III de Madrid, 2024).

---

## 1. Introduction

This project develops a **reinforcement learning agent** capable of playing the classic *Snake Game* using the **Q-learning** algorithm.  
The implementation is fully written in Python, leveraging **PyGame** for the graphical environment and **NumPy** for numerical computation.

The primary goal is to teach an autonomous agent to balance exploration and exploitation while maximizing rewards through self-play.

---

## 2. Approach Overview

Two major development phases were completed during experimentation:

### **Phase A – Initial Model**

**State Representation**
- **Direction**: Current heading of the snake (`UP`, `DOWN`, `LEFT`, `RIGHT`)
- **Optimal Move**: Direction minimizing Manhattan distance to the food
- Q-table size: **4 × 4 = 16 states**

**Reward Function**
| Event | Reward |
|--------|---------|
| Eats food | +10 |
| Moves closer to food | +1 |
| Moves away from food | −1 |
| Dies (collision) | −8 |

**Observations**
- The agent achieved limited success: it learned basic food-seeking behavior but failed when its body grew.
- The oversimplified state space prevented the model from capturing environment complexity.

---

### **Phase B – Enhanced Model**

**Improved State Definition**
| Component | Description | Values |
|------------|-------------|---------|
| **Direction** | Snake’s current movement | 4 |
| **to_food()** | Cardinal relation of food to head | 9 |
| **will_collide()** | Encoded nearby collisions with walls or body | 15 |

→ Total possible states: **4 × 9 × 15 = 540**

**Reward Function**
Unchanged from Phase A, still encouraging food proximity and penalizing collisions.

**Q-learning Parameters**
| Parameter | Symbol | Value |
|------------|---------|--------|
| Learning rate | α | 0.5 |
| Discount factor | γ | 0.9 |
| Exploration rate | ε | 1.0 (decay = 0.9999) |
| Episodes | ≈ 4000 |

This richer state representation allowed the agent to better predict outcomes and develop longer survival strategies.

---

## 3. Training Setup

- **Board sizes tested:** 150×150 px, 300×300 px, 500×500 px  
- **Snake growth:** both fixed-length and growing body modes  
- **Exploration–exploitation:** achieved via ε-decay, transitioning gradually from random actions to optimal policy exploitation.

The agent continuously updates a **Q-table** stored in `src/q_table.txt`, mapping state–action pairs to expected rewards.

---

## 4. Results and Observations

After extending the state space, the agent showed significant performance gains.

| Board Size | Mean Snake Length (50 Episodes) |
|-------------|---------------------------------|
| 150×150 | ≈ 25 |
| 300×300 | ≈ 43 |
| 500×500 | ≈ 53 |

**Key Insights**
- Expanding from 16 → 540 states dramatically improved learning depth.
- The richer representation enhanced the snake’s ability to plan around obstacles.
- Some extremely rare states remained unreached (e.g., being fully surrounded), which is acceptable trade-off for better expressiveness.

---

## 5. Conclusions

- **State design quality** is critical: richer, more descriptive features yield better decisions.  
- Larger Q-tables improve policy learning but require more episodes and memory.  
- Proper **reward shaping** (+1/−1 heuristics) accelerates convergence.  
- The final agent achieved stable, generalizable play across different board sizes.

---

## 6. Acknowledgements

This project is based on academic coursework completed for *Machine Learning I* at **Universidad Carlos III de Madrid**.  
Code foundation credited to **J.L.P.**, with adaptation and documentation prepared by **Felipe Grima Rodríguez**  
in collaboration with **Pedro Javier López Dondarza** for educational and portfolio purposes.

---
