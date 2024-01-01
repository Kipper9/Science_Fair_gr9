from Game import DotsAndBoxes
import neat
import os
import pickle
import random

class AI:
  def __init__(self,r, c):
    self.game = DotsAndBoxes(r,c)
    self.r =  r
    self.c = c
    self.used = set()

  def test_ai(self, genome, config):
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    while not self.game.isGameOver():
      turn = 1

      while turn == 1:
        p1_move = [int(input('What row: ')),int(input('What column: '))]
        state = self.game.gameStep(p1_move, turn)
        self.game.draw_board(turn)
        pos = self.game.invert_move(p1_move)
        self.used.add(pos)
        print()
        if state[1] == True:
          turn = 2
          self.game.isTurnOver = False
        if state[2] == True:
          break

      self.turns(net, 2)
      self.game.draw_board(turn)
      print()
    
    print('Score:',state[0])

  def train_AI(self,genome1,genome2,config):
    net1 = neat.nn.FeedForwardNetwork.create(genome1,config)
    net2 = neat.nn.FeedForwardNetwork.create(genome2,config)

    while True:
      self.turns(net1, 1)
      
      if self.game.isGameOver():
        self.calculate_fitness(genome1, genome2, self.game.points[0], self.game.points[1])
        self.game.reset()
        break
      
      self.game.isTurnOver = False

      self.turns(net2, 2)
      
      if self.game.isGameOver():
        self.calculate_fitness(genome1, genome2, self.game.points[0], self.game.points[1])
        self.game.reset()
        break
      
      self.game.isTurnOver = False
  
  def turns(self, net, turn):
    state = [0,0,0,0,0]
    while not self.game.isTurnOver:
      output = net.activate(self.game.ai_input())

      newoutput = self.remove_used(output)

      decision = newoutput.index(max(newoutput))
      
      if decision in self.used:
        rangea = 40 - len(self.used)
        print(rangea)
        self.game.draw_board(turn)
        lista = list(self.used)
        lista.sort
        decision = random.randint(0, rangea)
        for i in lista:
          if i <= decision:
            decision += 1
      
      self.used.add(decision)

      move = self.interpret_input(decision)

      state = self.game.gameStep(move, turn)
      
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

  def calculate_fitness(self, genome1, genome2, points1, points2):
    genome1.fitness += points1
    genome2.fitness += points2

def eval_genomes(genomes,config):
  width,height = 5,5
  games_played = 0
  for i,(genome_id1, genome1) in enumerate(genomes):
    if i  == len(genomes) - 1:
      break
    if genome1.fitness == None:
      genome1.fitness = 0

    for genome_id2,genome2 in genomes[i + 1:]:
      if genome2.fitness == None:
        genome2.fitness = 0

      game = AI(width,height)
      print('New Game!')
      game.train_AI(genome1,genome2,config)
      games_played += 1
  print(games_played)

def run_neat(config):
  #p = neat.Checkpointer.restore_checkpoint("neat-checkpoint-11")
  p = neat.Population(config)
  p.add_reporter(neat.StdOutReporter(True))
  stats = neat.StatisticsReporter()
  p.add_reporter(stats)
  p.add_reporter(neat.Checkpointer(1))

  winner = p.run(eval_genomes, 50)
  with open ('best.pickle','wb') as f:
    pickle.dump(winner, f)

def test_AI(config):
  with open('best.pickle','rb') as f:
    winner = pickle.load(f)

  game = AI(5,5)

  game.test_ai(winner, config)


if __name__ == "__main__":
  local_dir = os.path.dirname(__file__)

  config_path = os.path.join(local_dir, "config.txt")

  config = neat.Config(neat.DefaultGenome,neat.DefaultReproduction,\
    neat.DefaultSpeciesSet,neat.DefaultStagnation,config_path)
  
  run_neat(config)
