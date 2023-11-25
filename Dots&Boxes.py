Empty = 0

line_Team_1 = 1
line_Team_2 = 2

Team_points = [0,0]
completeSquares = 0

Team = 1
Grid = [
   [0,0,0,0],
  [0,0,0,0,0],
   [0,0,0,0],
  [0,0,0,0,0],
   [0,0,0,0],
  [0,0,0,0,0],
   [0,0,0,0],
  [0,0,0,0,0],
   [0,0,0,0]
  ]

def game_over():
  if completeSquares == 16:
    return True
  else:
    return False

def draw_Board():
  for i in Grid:
    print(i)

def click(row, col, turn):
  if Grid[row][col] == 1 or Grid[row][col] == 2:
    print("There is already a line there.")

  else:
    Grid[row][col] = turn
    
    if len(Grid[row]) == 4:
      if Grid[row-1][col] != 0 and Grid[row-1][col+1] != 0 and Grid[row-2][col] != 0:
        Team_points[turn - 1] =+ 1
        print("1 point for team", turn)
        completeSquares += 1
    
      if Grid[row+1][col] != 0 and Grid[row+1][col+1] != 0 and Grid[row+2][col] != 0:
        Team_points[turn - 1] =+ 1
        print("1 point for team", turn)
        completeSquares += 1
    
    if len(Grid[row]) == 5:
      if Grid[row][col-1] != 0 and Grid[row-1][col-1] != 0 and Grid[row+1][col-1] != 0:
        Team_points[turn - 1] =+ 1
        print("1 point for team",turn)
        completeSquares += 1

      if Grid[row-1][col] != 0 and Grid[row+1][col] != 0 and Grid[row][col+1] != 0:
        Team_points[turn - 1] =+ 1
        print("1 point for team", turn)
        completeSquares += 1

def play():
  Turn = 1
  while game_over != True:
    print("Player",Turn,"'s move")
    r = int(input("What row would you like to play: ")) - 1
    c = int(input("What column would you like to play: ")) - 1
    click(r,c,Turn)
    draw_Board()
    Turn = -1 * Turn + 3
  print("Game over")
  if Team_points[1] > Team_points[0]:
    print("Team 2 wins!")

  elif Team_points[1] < Team_points[0]:
    print("Team 1 wins!")
  
  elif Team_points[1] == Team_points[0]:
    print("Tie, no one wins :(")


play()