from Game import DotsAndBoxes
import neat
import os
class AI:
  def __init__(self,r, c):
    self.game = DotsAndBoxes(r,c)
    self.r =  r
    self.c = c

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
    
    turn = 1
    run = True
    while run:
      while turn == 1:
        output1 = net1.activate(self.game.ai_input())

        decision1 = output1.index(max(output1))

        move1 = self.interpret_input(decision1)
        print(move1)
        state = self.game.gameStep(move1, turn)

        self.game.draw_board()
        if state[2] == True:
          self.calculate_fitness(genome1,genome2,state)
          break
        if state[1] == True:
          turn = 2
      
      while turn == 2:
        output2 = net2.activate(self.game.ai_input())

        decision2 = output2.index(max(output2))

        move2 = self.interpret_input(decision2)
        state = self.game.gameStep(move2, turn)

        self.game.draw_board()
        if state[2] == True:
          self.calculate_fitness(genome1,genome2,state)
          break
        if state[1] == True:
          turn = 1

  def interpret_input(self,input):
    r = 0
    x = 0 
    while x < input:
      if r % 2 == 1:
        x += self.c - 1
      if r % 2 == 0:
        x += self.c
      r += 1
    
    if r % 2 == 1:
        x -= self.c - 1
    if r % 2 == 0:
        x -= self.c

    c = input - x
    return [r - 1,c - 1]

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