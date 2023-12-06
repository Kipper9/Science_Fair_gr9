class DotsAndBoxes:
  def __init__(self,move,gameSate,turn):
    self.grid = gameSate
    self.turn = turn
    self.completeSquares = 0
    self.points = [0,0]
    self.rows = len(gameSate)
    self.cols = len(gameSate[1])
    self.isTurnOver = False
    self.move = move
    self.gameState = gameSate

  def makeGrid(self):
    grid = []
    for i in range(0,self.rows):
      grid.append([])
      if i%2 == 0:
        for x in range(0,self.cols-1):
          self.grid[i].append(0)
      else:
        for x in range(0,self.cols):
          grid[i].append(0)
    return grid

  def isGameOver(self):
    if self.completeSquares == (self.rows - 1) * (self.cols - 1):
      return True
    else:
      return False

  def draw_Board(self):
    print("Board:")
    for i in self.grid:
      print(i)

  def click(self, row, col):
    
    if row > self.rows + 1 or col >= len(self.grid[row]):
      print('Invalid move')
      self.isTurnOver = False 

    elif self.grid[row][col] == 1 or self.grid[row][col] == 2:
      print("There is already a line there.")
      self.isTurnOver = False

    else:
      self.grid[row][col] = self.turn
      self.isTurnOver = True
      if len(self.grid[row]) == self.cols-1:
        if row != 0:
          if self.grid[row-1][col] != 0 and self.grid[row-1][col+1] != 0 and self.grid[row-2][col] != 0:
            self.points[self.turn - 1] += 1
            print("1 point for team", self.turn)
            self.completeSquares += 1
            self.isTurnOver = False

        if row < self.rows-1:
          if self.grid[row+1][col] != 0 and self.grid[row+1][col+1] != 0 and self.grid[row+2][col] != 0:
            self.points[self.turn - 1] += 1
            print("1 point for team", self.turn)
            self.completeSquares += 1
            self.isTurnOver = False

      if len(self.grid[row]) == self.cols:
        if col != 0:
          if self.grid[row][col-1] != 0 and self.grid[row-1][col-1] != 0 and self.grid[row+1][col-1] != 0:
            self.points[self.turn - 1] += 1
            print("1 point for team",self.turn)
            self.completeSquares += 1
            self.isTurnOver = False

        if col < self.cols-1:
          if self.grid[row-1][col] != 0 and self.grid[row+1][col] != 0 and self.grid[row][col+1] != 0:
            self.points[self.turn - 1] += 1
            print("1 point for team", self.turn)
            self.completeSquares += 1
            self.isTurnOver = False

  def play(self):
    self.click(self.move[0] - 1,self.move[1] - 1)
    self.draw_Board()
    return self.gameState, self.points, self.isTurnOver, self.isGameOver()
    