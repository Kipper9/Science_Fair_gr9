from Game import DotsAndBoxes
import neat
import os
import time
class AI:
  def __init__(self,r, c):
    self.game = DotsAndBoxes(r,c)
    self.r =  r
    self.c = c
    self.used = set()

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

  def train_AI(self,genome1,genome2,config):
    net1 = neat.nn.FeedForwardNetwork.create(genome1,config)
    net2 = neat.nn.FeedForwardNetwork.create(genome2,config)

    run = True
    while run:
      self.turns(net1, 1)
      
      if self.game.isGameOver():
        self.calculate_fitness(net1, net2)
        self.game.reset()
        run = False
      
      self.game.isTurnOver = False

      time.sleep(1)

      self.turns(net2, 2)
      
      if self.game.isGameOver():
        self.calculate_fitness(net1, net2)
        self.game.reset()
        run = False
      
      self.game.isTurnOver = False

      time.sleep(1)
  
  def turns(self, genome, turn):
    while not self.game.isTurnOver:
      output = genome.activate(self.game.ai_input())

      newoutput = self.remove_used(output)

      decision = newoutput.index(max(newoutput))

      print(decision)

      self.used.add(decision)

      move = self.interpret_input(decision)

      self.game.gameStep(move, turn)

      self.game.draw_board()
      print()
      print(f'Player ',turn,"'s move")

  def remove_used (self, output):
    for i, v in enumerate(output):
      if i in self.used:
        output[i] = 0
        
    return output

  def interpret_input(self,input1):
    row = 0
    x = 0
    n = 3

    while x + n < input1:
      if row % 2 == 0:
        x += self.c - 1
        n = 4
      else:
        x += self.c
        n = 3
      
      row += 1
    
    col = input1 - x

    return [row, col]

  def calculate_fitness(self, genome1, genome2, game_info):
    pass

def eval_genomes(genomes,config,):
  width,height = 5,5
  for i,(genome_id1, genome1) in enumerate(genomes):
    if i  == len(genomes) - 1:
      break

    genome1.fitness = 0

    for genome_id2,genome2 in genomes[i+1:]:
      genome2.fitness = 0 if genome2.fitness == None else genome2.finess

      game = AI(width,height)
      game.train_AI(genome1,genome2,config)

def run_neat(config):
  # p = neat.Checkpointer.restore_checkpoint("neat-checkpointer-")
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