import pygame
from Game import DotsAndBoxes
from NeatAI import AI
import pickle
import neat
import os
import random
import time

class Game:
  def __init__(self, rows, cols, config):
    self.score_board = pygame.font.SysFont("comicsans", 50)
    self.trainer = AI(rows,cols)
    self.w = (cols + 1) * 100
    self.h = (rows + 1) * 100
    self.window = pygame.display.set_mode((self.w, self.h))
    self.run = True
    self.dots = self.create_dots(cols, rows)
    self.vert_line = [5,80]
    self.hori_line = [80,5]
    self.black = (0,0,0)
    self.blue = (0,0,255)
    self.red = (255,0,0)
    self.white = (255,255,255)
    self.turn = 1
    self.winner = False
    self.config = config
    self.state = False

  def create_dots(self, c, r):
    grid = []
    for i in range(c):
      grid.append([])
      for x in range(r):
        grid[i].append([(100 * i + 100, x * 100 + 100), 10])
    return grid

  def get_genome(self):
    with open('data/genome_.pickle','rb') as f:
      self.winner = pickle.load(f)

  def draw_board(self):
    self.window.fill(self.white)
    left_score_text = self.score_board.render(
      f'{self.trainer.game.points[0]}', 1, self.black
    )
    right_score_text = self.score_board.render(
      f'{self.trainer.game.points[1]}', 1, self.black
    )
    WIDTH = self.w
    self.window.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    self.window.blit(right_score_text, (WIDTH * (3/4) -
                                right_score_text.get_width()//2, 20))
    for i in self.dots:
      for x in i:
        pygame.draw.circle(self.window, self.black, x[0],x[1])
    
    for val, i in enumerate(self.trainer.game.grid):
      for id, x in enumerate(i):
        if x == 1:
          if val % 2 == 0:
            pygame.draw.rect(self.window, self.black, (110 + (100 * id), 97.5 + (100 * (val // 2)), self.hori_line[0], self.hori_line[1]))
          
          if val % 2 == 1:
            pygame.draw.rect(self.window, self.black,(97.5 + (100 * id), 110 + (100 * (val // 2)), self.vert_line[0], self.vert_line[1]))

    pygame.display.update()

  def ai_game_loop (self):
    while self.run:
      self.draw_board()
      while self.turn == 1:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            self.run = False
          
          elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print("x:", mouse_x)
            print('y:',mouse_y)
            position = self.get_clicked_line(mouse_x,mouse_y)
            print()
            print('pos:',position)

            if position:
              self.state = self.trainer.game.gameStep(position,self.turn)
              self.trainer.game.draw_board(self.turn)

              self.draw_board()
              
              if self.trainer.game.isTurnOver == True:
                self.turn = 2
              
              if self.state[2] == True:
                self.run = False
          
      net = neat.nn.FeedForwardNetwork.create(self.winner,self.config)

      self.trainer.game.isTurnOver = False

      self.trainer.turns(net,2)
      self.turn = 1
      if self.state[2] == True:
        self.run = False
  
  def normal_game_loop(self):
    while self.run:
      self.draw_board()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.run = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
          mouse_x, mouse_y = pygame.mouse.get_pos()
          print("x:", mouse_x)
          print('y:',mouse_y)
          position = self.get_clicked_line(mouse_x,mouse_y)
          print()
          print('pos:',position)
          if position == False:
            pass
          else:
            state = self.trainer.game.gameStep(position,self.turn)
            self.trainer.game.draw_board(self.turn)
          
          if position:
            if state[1]:
              if self.turn == 1:
                self.turn = 2
              elif self.turn == 2:
                self.turn = 1
            
            if state[2] == True:
              self.run = False

  def test_ai_random(self):

    while self.run:
      self.draw_board()
      self.turn = 1
      while self.turn == 1:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            self.run = False

        if self.trainer.game.isGameOver():
          break

        rangea = 41 - len(self.trainer.used)

        lista = list(self.trainer.used)

        lista.sort()

        decision = random.randint(0, rangea)

        for i in lista:
          if i <= decision:
            decision += 1

        self.trainer.used.add(decision)

        move = self.trainer.interpret_input(decision)

        self.state = self.trainer.game.gameStep(move, self.turn)

        if self.state[1]:
          self.turn = 2
      
      if self.state[2] == True:
        self.run = False

      self.draw_board()
          
      net = neat.nn.FeedForwardNetwork.create(self.winner,self.config)

      self.trainer.game.isTurnOver = False

      self.trainer.turns(net,2)
      self.turn = 1
      if self.trainer.game.points[0] + self.trainer.game.points[1] == 9:
        self.run = False
    points = self.trainer.game.points
    self.run = True
    self.trainer.used = set()
    self.trainer.game.reset()
    return points
  
  def get_clicked_line(self,x,y):
    if x < 90 or x > (self.w - 90):
      return False
    elif y < 90 or y > (self.h - 90):
      return False

    col, width_1 = self.get_axis_val(x)
    row, width_2 = self.get_axis_val(y)

    if width_1 == width_2:
      return False

    if row % 2 == 1:
      col = col // 2

    if row % 2 == 0:
      col = col // 2

    return [row, col] 
  
  def get_axis_val(self,x):
    col = 0
    t = 0
    width = 20  
    while t + width < x -100:
      if col % 2 == 0:
        t += 20
        width = 80
      else:
        t += 80
        width = 20
      
      col += 1
    return col, width

def test_ai(game):
  ave = 0
  wins = 0
  totalpoints = 0
  for i in range(0,1001):
    points = game.test_ai_random()
    
    if points[0] < points[1]:
      wins += 1

    totalpoints += points[1]
    ave = (ave + points[1]) / (i + 1)
    
  
  print(f"The AI averaged {ave} points per game agains't a randomized player")
  print(f"The AI totaled {totalpoints} points")
  print(f"The AI won {wins} times agains't a randomized player")


pygame.init()

local_dir = os.path.dirname(__file__)

config_path = os.path.join(local_dir, "data/new-config.txt")

config = neat.Config(neat.DefaultGenome,neat.DefaultReproduction,\
    neat.DefaultSpeciesSet,neat.DefaultStagnation,config_path)

game = Game(4, 4, config)

game.get_genome()
# game.normal_game_loop()
game.ai_game_loop()
# test_ai(game)



pygame.quit()