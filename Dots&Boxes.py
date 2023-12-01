Turn_over = False
Team_points = [0,0]
completeSquares = 0
Grid = []
def MakeGrid(R,C):
  global Grid
  for i in range(0,R):
    Grid.append([])
    if i%2 == 0:
      for x in range(0,C-1):
        Grid[i].append(0)
    else:
      for x in range(0,C):
        Grid[i].append(0)
  return Grid
def game_over(m):
  global Turn_over
  global completeSquares
  global Grid
  if completeSquares == m:
    Turn_over = True
    return True
  else:
    return False
def draw_Board():
  print("Board:")
  for i in Grid:
    print(i)
def click(row, col, turn,r,c):
  global completeSquares
  global Turn_over
  global Grid
  if row > r+1 or col > c+1:
    print('Invalid move')
    Turn_over = False 
  elif Grid[row][col] == 1 or Grid[row][col] == 2:
    print("There is already a line there.")
    Turn_over = False
  else:
    Grid[row][col] = turn
    Turn_over = True
    if len(Grid[row]) == c-1:
      if row != 0:
        if Grid[row-1][col] != 0 and Grid[row-1][col+1] != 0 and Grid[row-2][col] != 0:
          Team_points[turn - 1] =+ 1
          print("1 point for team", turn)
          completeSquares += 1
          Turn_over = False
      if row < r-1:
        if Grid[row+1][col] != 0 and Grid[row+1][col+1] != 0 and Grid[row+2][col] != 0:
          Team_points[turn - 1] =+ 1
          print("1 point for team", turn)
          completeSquares += 1
          Turn_over = False
    if len(Grid[row]) == c:
      if col != 0:
        if Grid[row][col-1] != 0 and Grid[row-1][col-1] != 0 and Grid[row+1][col-1] != 0:
          Team_points[turn - 1] =+ 1
          print("1 point for team",turn)
          completeSquares += 1
          Turn_over = False
      if col < c-1:
        if Grid[row-1][col] != 0 and Grid[row+1][col] != 0 and Grid[row][col+1] != 0:
          Team_points[turn - 1] =+ 1
          print("1 point for team", turn)
          completeSquares += 1
          Turn_over = False
def play():
  global Grid
  global Team_points
  global Turn_over
  Rows = int(input('How many rows: '))
  Cols = int(input('How many Columns: '))
  MaxSquares = (Rows-1)*(Cols-1)
  Rows = (Rows - 1) * 2 + 1
  Grid = MakeGrid(Rows,Cols)
  Turn = 1
  while not game_over(MaxSquares):
    while Turn_over == False:
        print()
        print("Player",Turn,"'s move")
        print()
        r = int(input("What row would you like to play: ")) - 1
        c = int(input("What column would you like to play: ")) - 1
        click(r,c,Turn,Rows,Cols)
        print()
        draw_Board()
        if game_over(MaxSquares):
          Turn_over = True
    Turn_over = False
    Turn = -1 * Turn + 3
  print()
  print("Game over")
  print()
  if Team_points[1] > Team_points[0]:
    print("Team 2 wins!")
  elif Team_points[1] < Team_points[0]:
    print("Team 1 wins!") 
  elif Team_points[1] == Team_points[0]:
    print("Tie, no one wins :(")
  for i in range(0,2):
    print('Team',i+1,'got',Team_points[i])
play()