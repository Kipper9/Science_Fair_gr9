from Game import DotsAndBoxes
import neat
import os
class AI:
  def __init__(self,r, c):
    self.game = DotsAndBoxes(r,c)

  def test_ai(self):
    while not self.game.isGameOver():
      turn = 1

      while turn == 1:
        p1_move = [int(input('What row: ')) - 1,int(input('What column: ')) - 1]
        state = self.game.gameStep(p1_move,turn)
        self.game.draw_board()
        if state[1] == True:
          turn = 2
        if state[2] == True:
          break

      while turn == 2:
        p2_move = [int(input('What row: ')) - 1,int(input('What column: ')) - 1]
        state = self.game.gameStep(p2_move,turn)
        self.game.draw_board()
        if state[1] == True:
          turn = 1
        if state[2] == True:
          break
    
    print('Score:',state[0])
  
def eval_genomes(genomes,config,):
  pass

def run_neat(config):
  # p = neat.Checkpointer.restore_checkpoint("neat-checkpointer-#")
  p = neat.Population(config)
  p.add_reporter(neat.StdOutReporter(True))
  stats = neat.StatisticsReporter()
  p.add_reporter(stats)
  p.add_reporter(neat.Checkpointer(1))

  winner = p.run(eval_genomes, 50)

if __name__ == "__main__":
  local_dir = os.path.dirname(__file__)

  config_path = os.path.join(local_dir, "config.txt")

  config = neat.Config(neat.DefaultGenome,neat.DefaultReproduction,\
    neat.DefaultSpeciesSet,neat.DefaultStagnation,config_path)
  
  run_neat(config)