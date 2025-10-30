"""
Project: Reinforcement Learning Snake Agent
File: snake_env.py
Snake Eater Environment

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
import numpy as np
import random

class SnakeGameEnv:
    def __init__(self, frame_size_x=150, frame_size_y=150, growing_body=True):
        # Initializes the environment with default values
        self.frame_size_x = frame_size_x
        self.frame_size_y = frame_size_y
        self.growing_body = growing_body
        self.reset()

    def reset(self):
        # Resets the environment with default values
        self.snake_pos = [50, 50]
        self.snake_body = [[50, 50], [60, 50], [70, 50]]
        self.food_pos = [random.randrange(1, (self.frame_size_x // 10)) * 10, random.randrange(1, (self.frame_size_y // 10)) * 10]
        self.food_spawn = True
        self.direction = 'RIGHT'
        self.score = 0
        self.game_over = False
        return self.get_state()

    def step(self, action):
        # Implements the logic to change the snake's direction based on action
        # Update the snake's head position based on the direction
        # Check for collision with food, walls, or self
        # Update the score and reset food as necessary
        # Determine if the game is over
        prev_distance = abs(self.snake_pos[0] - self.food_pos[0]) + abs(
            self.snake_pos[1] - self.food_pos[1])
        self.update_snake_position(action)
        reward = self.calculate_reward(prev_distance)
        self.update_food_position()
        state = self.get_state()
        self.game_over = self.check_game_over()
        return state, reward, self.game_over

    def get_state(self):
        # Your code here
        # Here, you will calculate the state based on your actual state calculation logic

        state = (self.direction, self.to_food(), self.will_collide())
        return state
        
    def get_body(self):
        return self.snake_body

    def get_food(self):
        return self.food_pos
    
    def to_food(self):
        snake_x, snake_y = self.snake_pos
        food_x, food_y = self.get_food()
        if snake_x == food_x and snake_y == food_y:
            return 'EAT'
        if snake_x < food_x:
            if snake_y < food_y:
                return 'SOUTH-EAST'
            elif snake_y > food_y:
                return 'NORTH-EAST'
            return 'EAST'
        elif snake_x > food_x:
            if snake_y < food_y:
                return 'SOUTH-WEST'   
            elif snake_y > food_y:
                return 'NORTH-WEST'  
            return 'WEST'
        if snake_y < food_y:
            return 'SOUTH'
        elif snake_y > food_y:
            return 'NORTH'
        
        #directions = {'EAT': 0, 'NORTH': 1, 'SOUTH': 2, 'WEST': 3, 'EAST': 4, 'NORTH-EAST': 5, 'NORTH-WEST': 6, 'SOUTH-EAST': 7, 'SOUTH-WEST': 8 }

    def next_moves(self):
        snake_x, snake_y = self.snake_pos
        return ([snake_x+10, snake_y],[snake_x-10,snake_y],[snake_x,snake_y-10],[snake_x,snake_y+10])

    def will_collide(self):
        fut_r, fut_l, fut_u, fut_d = self.next_moves()
        col_r = col_l = col_u = col_d = False
        
            #Collision with edges
        if fut_l[0] < 0:
            col_l = True
        elif fut_r[0] >= self.frame_size_x:
            col_r = True
        if fut_u[1] < 0:
            col_u = True
        elif fut_d[1] >= self.frame_size_y:
            col_d = True

            #Collision with body
        for block in self.snake_body[1:]:
            if fut_r == block:
                col_r = True
            if fut_l == block:
                col_l = True
            if fut_u == block:
                col_u = True
            if fut_d == block:
                col_d = True
        
            #Conversion to state
        states = []
        if col_r:
            states.append("RIGHT")
        if col_l:
            states.append("LEFT")
        if col_u:
            states.append("UP")
        if col_d:
            states.append("DOWN")
        if not states:
            return "RIGHT"
        return "-".join(sorted(states))


        #collision_states = {'DOWN': 0, 'LEFT': 1, 'RIGHT': 2, 'UP': 3, 'DOWN-LEFT': 4, 'DOWN-RIGHT': 5, 'DOWN-UP': 6, 'LEFT-RIGHT': 7, 'LEFT-UP': 8, 'RIGHT-UP': 9, 'DOWN-LEFT-RIGHT': 10, 'DOWN-LEFT-UP': 11, 'DOWN-RIGHT-UP': 12, 'LEFT-RIGHT-UP': 13, 'DOWN-LEFT-RIGHT-UP': 14}

    def calculate_reward(self, prev_distance):
        # Your code here
        # Calculate and return the reward. Remember that you can provide possitive or negative reward.
        reward = 0
        current_distance = abs(self.snake_pos[0] - self.food_pos[0]) + abs(
            self.snake_pos[1] - self.food_pos[1])
        if self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] == self.food_pos[1]:
            reward = 10
        elif current_distance < prev_distance:
            reward = 1
        elif current_distance > prev_distance:
            reward = -1
        elif current_distance == prev_distance:
            reward = 0
        if self.check_game_over():
            reward = -8

        return reward
    
    def getLegalActions(self, state):

        "Checks if moving in the given direction will result in a collision."
        legalActions = []
        snake_x, snake_y = self.snake_pos
        direction = state
    
        if direction == 'UP':
            snake_y -= 10
        elif direction == 'DOWN':
            snake_y += 10
        elif direction == 'LEFT':
            snake_x -= 10
        elif direction == 'RIGHT':
            snake_x += 10

        next_pos_UP = [snake_x, snake_y - 10]
        next_pos_DOWN = [snake_x, snake_y + 10]
        next_pos_LEFT = [snake_x - 10, snake_y]
        next_pos_RIGHT = [snake_x + 10, snake_y]

        if next_pos_UP not in self.snake_body and next_pos_UP[1] >= 0:
            legalActions.append(0)
        if next_pos_DOWN not in self.snake_body and next_pos_DOWN[1] <= self.frame_size_y-10:
            legalActions.append(1)
        if next_pos_LEFT not in self.snake_body and next_pos_LEFT[0] >= 0:
            legalActions.append(2)
        if next_pos_RIGHT not in self.snake_body and next_pos_RIGHT[0] <= self.frame_size_x-10:
            legalActions.append(3)
        if legalActions == []:
            return [0, 1, 2, 3]
        return legalActions

    def check_game_over(self):
        # Return True if the game is over, else False
        if self.snake_pos[0] < 0 or self.snake_pos[0] > self.frame_size_x-10:
            return True
        if self.snake_pos[1] < 0 or self.snake_pos[1] > self.frame_size_y-10:
            return True
        for block in self.snake_body[1:]:
            if self.snake_pos[0] == block[0] and self.snake_pos[1] == block[1]:
                return True
                
        return False

    def update_snake_position(self, action):
        # Updates the snake's position based on the action
        # Map action to direction
        change_to = ''
        direction = self.direction
        if action == 0:
            change_to = 'UP'
        elif action == 1:
            change_to = 'DOWN'
        elif action == 2:
            change_to = 'LEFT'
        elif action == 3:
            change_to = 'RIGHT'
    
        # Move the snake
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
    
        if direction == 'UP':
            self.snake_pos[1] -= 10
        elif direction == 'DOWN':
            self.snake_pos[1] += 10
        elif direction == 'LEFT':
            self.snake_pos[0] -= 10
        elif direction == 'RIGHT':
            self.snake_pos[0] += 10
            
        self.direction = direction
        
        
        self.snake_body.insert(0, list(self.snake_pos))
        
        if self.snake_pos[0] == self.food_pos[0] and self.snake_pos[1] == self.food_pos[1]:
            self.score += 10
            self.food_spawn = False
            # If the snake is not growing
            if not self.growing_body:
                self.snake_body.pop()
        else:
            self.snake_body.pop()
    
    def update_food_position(self):
        if not self.food_spawn:
            self.food_pos = [random.randrange(1, (self.frame_size_x//10)) * 10, random.randrange(1, (self.frame_size_x//10)) * 10]
        self.food_spawn = True