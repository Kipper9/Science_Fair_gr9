class DotsAndBoxes:
  def __init__(self,r,c):
    self.points = [0,0]
    self.rows = r
    self.cols = c
    self.isTurnOver = False
    self.grid = self.makeGrid()
    self.isMoveValid = True

  def makeGrid(self):
    grid = []
    for i in range(0,(self.rows-1)*2+1):
      grid.append([])
      if i%2 == 0:
        for x in range(0,self.cols-1):
          grid[i].append(0)
      else:
        for x in range(0,self.cols):
          grid[i].append(0)
    return grid

  def ai_input(self):
    output = []
    for i in self.grid:
      for x in i:
        output.append(x)
    return output

  def open_box_count(self):
    y = 0

    checks = [
      [0,0],
      [1,0],
      [1,1],
      [2,0],
      ]
    
    total_count = 0

    layer = 0

    for i in range(0,9):
      count = 0
      for x in checks:
        if self.grid[x[0] + layer][x[1] + (i - y)] == 0:
          count += 1

        if count == 2:
          break

      if count == 1:
        total_count += 1
      
      if (i+1) % 3 == 0 and i != 0:
        layer += 2
        y += 3
    return total_count

  def isGameOver(self):
    if  self.points[0] + self.points[1] == (self.rows - 1) * (self.cols - 1):
      return True
    else:
      return False

  def draw_board(self,turn):
    print()
    print(f"Player {turn}'s move")
    print()
    print('Score:')
    print(f'Team 1: {self.points[0]}')
    print(f'Team 2: {self.points[1]}')
    for i, v  in enumerate(self.grid):
      if i % 2 == 0:
        print(f' ',v)
      else:
        print(v)
    if self.isTurnOver:
      print()
      print('Their turn is over')

  def invert_move(self, move):
    output = 0
    for i in range(0, move[0]):
      if i % 2 == 0:
        output += self.cols - 1
      if i % 2 == 1:
        output += self.cols
    
    if move[0] % 2 == 0:
      output = output - (self.cols - 1 - move[1])
    if move[0] % 2 == 1:
      output = output - (self.cols - move[1])

  def click(self, row, col,turn):
    
    if row > self.rows * 2 - 2 or col >= len(self.grid[0 if row % 2 == 0 else 1]) or row < 0 or col < 0:
      self.isTurnOver = False 
      pass

    elif self.grid[row][col] == 1:
      self.isTurnOver = False
      self.isMoveValid = False
      pass

    else:
      self.grid[row][col] = 1
      self.isTurnOver = True
      if len(self.grid[row]) == self.cols-1:
        if row != 0:
          if self.grid[row-1][col] != 0 and self.grid[row-1][col+1] != 0 and self.grid[row-2][col] != 0:
            self.points[turn - 1] += 1
            self.isTurnOver = False

        if row < self.rows * 2 - 2:
          if self.grid[row+1][col] != 0 and self.grid[row+1][col+1] != 0 and self.grid[row+2][col] != 0:
            self.points[turn - 1] += 1
            self.isTurnOver = False

      if len(self.grid[row]) == self.cols:
        if col != 0:
          if self.grid[row][col-1] != 0 and self.grid[row-1][col-1] != 0 and self.grid[row+1][col-1] != 0:
            self.points[turn - 1] += 1
            self.isTurnOver = False

        if col < self.cols - 1:
          if self.grid[row-1][col] != 0 and self.grid[row+1][col] != 0 and self.grid[row][col+1] != 0:
            self.points[turn - 1] += 1
            self.isTurnOver = False
            
  def gameStep(self,action,turn):
    self.click(action[0],action[1],turn)
    return self.points, self.isTurnOver, self.isGameOver(), self.grid, self.isMoveValid
  
  def reset(self):
    self.points = [0,0]
    self.isTurnOver = False
    self.grid = self.makeGrid()
