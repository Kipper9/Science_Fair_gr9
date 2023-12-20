class DotsAndBoxes:
  def __init__(self,r,c):
    self.completeSquares = 0
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

  def isGameOver(self):
    if self.completeSquares == (self.rows - 1) * (self.cols - 1):
      return True
    else:
      return False

  def draw_board(self):
    for i  in self.grid:
      print(i)

  def click(self, row, col,turn):
    
    if row > self.rows + 1 or col >= len(self.grid[row]):
      print('Invalid move')
      self.isTurnOver = False 

    elif self.grid[row][col] == 1 or self.grid[row][col] == 2:
      print("There is already a line there.")
      self.isTurnOver = False
      self.isMoveValid = False

    else:
      self.grid[row][col] = turn
      self.isTurnOver = True
      if len(self.grid[row]) == self.cols-1:
        if row != 0:
          if self.grid[row-1][col] != 0 and self.grid[row-1][col+1] != 0 and self.grid[row-2][col] != 0:
            self.points[turn - 1] += 1
            print("1 point for team", turn)
            self.completeSquares += 1
            self.isTurnOver = False

        if row < self.rows-1:
          if self.grid[row+1][col] != 0 and self.grid[row+1][col+1] != 0 and self.grid[row+2][col] != 0:
            self.points[turn - 1] += 1
            print("1 point for team", turn)
            self.completeSquares += 1
            self.isTurnOver = False

      if len(self.grid[row]) == self.cols:
        if col != 0:
          if self.grid[row][col-1] != 0 and self.grid[row-1][col-1] != 0 and self.grid[row+1][col-1] != 0:
            self.points[turn - 1] += 1
            print("1 point for team",turn)
            self.completeSquares += 1
            self.isTurnOver = False

        if col < self.cols-1:
          if self.grid[row-1][col] != 0 and self.grid[row+1][col] != 0 and self.grid[row][col+1] != 0:
            self.points[turn - 1] += 1
            print("1 point for team", turn)
            self.completeSquares += 1
            self.isTurnOver = False

  def gameStep(self,action,turn):
    self.click(action[0],action[1],turn)
    return self.points, self.isTurnOver, self.isGameOver(), self.grid, self.isMoveValid
  
  def reset(self):
    self.points = [0,0]
    self.isTurnOver = False
    self.grid = self.makeGrid()
