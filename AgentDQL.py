from Game import DotsAndBoxes
from collections import deque
import random
import numpy as np

Max_memory = 100_000
BatchSize = 1000
LR = 0.001

class Agent:
  def __init__(self):
    self.numGames = 0
    self.epsilon = 0
    self.gamma = 0
    self.memory = deque(maxlen = Max_memory)

  def getState(self,game):
    pass

  def remember(self,state,action,reward,next_state,game_over):
    pass

  def train_long_memory(self):
    pass

  def train_short_memory(self,state,action,reward,next_state,game_over):
    pass

  def get_action(self,state):
    pass

def train(grid):
  plot_score = []
  plot_mean_score = []
  total_score = 0
  record = 0
  agent = Agent()
  game = DotsAndBoxes(grid)
  while True:
    stateOld = agent.getState(game)

    finalMove = agent.get_action(stateOld)

    reward,done,score = game.play(finalMove)
    

if __name__ == '__main__':
  grid = [
    [0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0]
    ] #TODO
  train(grid)