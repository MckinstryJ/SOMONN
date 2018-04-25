<<<<<<< HEAD
from __future__ import print_function
import neat

def eval_genome(genome, config, inputs, outputs):
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    error = 4.0
    for xi, xo in zip(inputs, outputs):
        output = net.activate(xi)
        error -= (output[0] - xo) ** 2
    return error


def run(config_file, inputs, outputs):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Run for up to 300 generations.
    pe = neat.ParallelEvaluator(8, eval_genome, inputs, outputs)
    winner, fitness = p.run(pe.evaluate, 300)

    #return fitness of winner
=======
from __future__ import print_function
import neat

def eval_genome(genome, config, inputs, outputs):
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    error = 4.0
    for xi, xo in zip(inputs, outputs):
        output = net.activate(xi)
        error -= (output[0] - xo) ** 2
    return error


def run(config_file, inputs, outputs):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Run for up to 300 generations.
    pe = neat.ParallelEvaluator(8, eval_genome, inputs, outputs)
    winner, fitness = p.run(pe.evaluate, 300)

    #return fitness of winner
>>>>>>> 00b35791e129996c8b4cb60ebab20409eab81683
    return round(fitness, 4)