from NeatAI import AI
from Game import DotsAndBoxes

test = AI(5,5)

while not test.game.isGameOver():
  input1 = int(input('What spot: '))
  move = test.interpret_input(input1)
  print(move)
  print()
  test.game.gameStep(move, 1)
  test.game.draw_board()

  [
    [0,0],
    [0,0,0],
    [0,0],
    [0,0,0],
    [0,0]
    ]