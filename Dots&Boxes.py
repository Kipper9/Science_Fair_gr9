Empty = 0

line_Team_1 = 1
line_Team_2 = 2

Team_points = [0,0]


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

def click(row, col, turn):
  if Grid[row][col] == 1 or Grid[row][col] == 2:
    print("There is already a line there.")
    pass
  
  Grid[row][col] = turn
  
  if len(Grid[row]) == 4:
    if Grid[row][col] == turn and Grid[row-1][col] == turn and Grid[row-1][col] == turn and Grid[row-2][col] == turn:
      Team_points[turn] =+ 1
      print("1 point for team",turn)
  
    if Grid[row][col] == turn and Grid[row+1][col] == turn and Grid[row+1][col+1] == turn and Grid[row+2][col] == turn:
      Team_points[turn] =+ 1
      print("1 point for team",turn)
  
  # if len(Grid[row]) == 5:
  #   if Grid[row][col] == turn and Grid[row][col] == turn and Grid[row][col] == turn and Grid[row][col] == turn:
  #     Team_points[turn] =+ 1
  #     print("1 point for team",turn)
  
  #   if Grid[row][col] == turn and Grid[row][col] == turn and Grid[row][col] == turn and Grid[row][col] == turn:
  #     Team_points[turn] =+ 1
  #     print("1 point for team",turn)

click(2,1,1)
click(2,2,1)
click(3,1,1)
click(1,1,1)

for x in range(0,9):
  print(Grid[x])