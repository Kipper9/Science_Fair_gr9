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
    if Grid[row-1][col] != 0 and Grid[row-1][col+1] != 0 and Grid[row-2][col] != 0:
      Team_points[turn - 1] =+ 1
      print("1 point for team 1")
  
    if Grid[row+1][col] != 0 and Grid[row+1][col+1] != 0 and Grid[row+2][col] != 0:
      Team_points[turn - 1] =+ 1
      print("1 point for team 2")
  
  if len(Grid[row]) == 5:
    if Grid[row][col-1] != 0 and Grid[row-1][col-1] != 0 and Grid[row+1][col-1] != 0:
      Team_points[turn - 1] =+ 1
      print("1 point for team 3")

    if Grid[row-1][col] != 0 and Grid[row+1][col] != 0 and Grid[row][col+1] != 0:
      Team_points[turn - 1] =+ 1
      print("1 point for team 4")


click(0,0,1)
for x in range(0,9):
  print(Grid[x])
print("")

click(1,0,1)
for x in range(0,9):
  print(Grid[x])
print("")

click(2,0,1)
for x in range(0,9):
  print(Grid[x])
print("")

click(1,1,2)
for x in range(0,9):
  print(Grid[x])