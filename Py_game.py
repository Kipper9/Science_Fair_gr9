import pygame
from Game import DotsAndBoxes

pygame.init()

class Game:
  def __init__(self, rows, cols):
    self.game = DotsAndBoxes(rows, cols)
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

  def create_dots(self, c, r):
    grid = []
    for i in range(c):
      grid.append([])
      for x in range(r):
        grid[i].append([(100 * i + 100, x * 100 + 100), 10])
    return grid

  def draw_board(self):
    self.window.fill(self.white)
    for i in self.dots:
      for x in i:
        pygame.draw.circle(self.window, self.black, x[0],x[1])
    
    for val, i in enumerate(self.game.grid):
      for id, x in enumerate(i):
        if x == 1:
          if val % 2 == 0:
            pygame.draw.rect(self.window, self.black, (110 + (100 * id), 97.5 + (100 * (val // 2)), self.hori_line[0], self.hori_line[1]))
          
          if val % 2 == 1:
            pygame.draw.rect(self.window, self.black,(97.5 + (100 * id), 110 + (100 * (val // 2)), self.vert_line[0], self.vert_line[1]))

    pygame.display.update()

  def game_loop (self):
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
            state = self.game.gameStep(position,self.turn)
            self.game.draw_board(self.turn)
          
          if state[1]:
            if self.turn == 1:
              self.turn = 2
            elif self.turn == 2:
              self.turn = 1
          
          if state[2] == True:
            self.run = False

  
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


game = Game(int(input('How many rows: ')), int(input('How many colunms: ')))

game.game_loop()

pygame.quit()