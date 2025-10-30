"""
Project: Reinforcement Learning Snake Agent
File: SnakeGame.py
Snake Eater Game

Code base originally provided by J.L.P.
(Anonymized due to lack of formal permission to publish their full name.
Credit is acknowledged for the foundational implementation developed during
Machine Learning I, Universidad Carlos III de Madrid.)

Public version prepared and maintained by:
    Felipe Grima Rodríguez
    (with collaboration of Pedro Javier López Dondarza)

License: MIT License (for educational / portfolio demonstration only)

Notes:
- This repository is a sanitized and educational adaptation of a university project.
- The original author has been anonymized; all rights and credits are preserved.
- The project demonstrates the use of tabular Q-learning in a PyGame-based environment.
"""
from snake_env import SnakeGameEnv
from q_learning import QLearning
import pygame
import sys
import time


def main():
    # Window size
    FRAME_SIZE_X = 350
    FRAME_SIZE_Y = 350
    
    # Colors (R, G, B)
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)
    GREEN = pygame.Color(0, 255, 0)
    BLUE = pygame.Color(0, 0, 255)
    
    difficulty = 25  # Adjust as needed
    render_game = True # Show the game or not
    growing_body = True # Makes the body of the snake grow
    training = False # Defines if it should train or not

            # Initialize the game window, environment and q_learning algorithm
            # Your code here.
            # You must define the number of possible states.
    number_states = 4*9*15
    pygame.init()
    env = SnakeGameEnv(FRAME_SIZE_X, FRAME_SIZE_Y, growing_body)
    ql = QLearning(n_states=number_states, n_actions=4)  
    num_episodes = 50


    if render_game:
        game_window = pygame.display.set_mode((FRAME_SIZE_X, FRAME_SIZE_Y))
        fps_controller = pygame.time.Clock()
    
    for episode in range(num_episodes):
        state = env.reset()
        total_reward = 0
        game_over = False
        
        while not game_over:
            # Your code here.
            # Choose the best action for the state and possible actions from the q_learning algorithm
            # Call the environment step with that action and get next_state, reward and game_over variables
            state = env.get_state()
            stateIn = ql.getStateIndex(state)
            allowed_actions = env.getLegalActions(state)
            actionIn = ql.choose_action(stateIn, allowed_actions)
            action = list(ql.actions.keys())[actionIn]
            next_state, nreward, game_over = env.step(actionIn)
            if training:
                ql.update_q_table(state, action, nreward, next_state,
                                            env.check_game_over())
            state = env.get_state()
            total_reward += nreward
            
                
            # Update the state and the total_reward.
            
            # Render
            if render_game:
                game_window.fill(BLACK)
                snake_body = env.get_body()
                food_pos = env.get_food()
                for pos in snake_body:
                    pygame.draw.rect(game_window, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
        
                pygame.draw.rect(game_window, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
            
            if env.check_game_over():
                break

            if render_game:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                pygame.display.flip()
                fps_controller.tick(difficulty)
        
        ql.save_q_table()
        print(f"Episode {episode+1}, Total reward: {total_reward}, Total length: {len(snake_body)}")

if __name__ == "__main__":
    main()
