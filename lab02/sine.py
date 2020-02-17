"""
This module implements local search on a simple abs function variant.
The function is an absolute sine function

@author: kvlinden
@version 6feb2013
"""
import sys
sys.path.append('/home/neg6/cs344/cs344-code/tools/aima')
sys.path.append('/home/neg6/cs344/cs344-code/tools/paip')
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math


class SineVariant(Problem):
    """
    State: x value for the abs function variant sin(x)
    Move: a new x value delta steps from the current x (in both directions) 
    """
    
    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta
        
    def actions(self, state):
        return [state + self.delta, state - self.delta]
    
    def result(self, stateIgnored, x):
        return x
    
    def value(self, x):
        return math.fabs(x * math.sin(x))


if __name__ == '__main__':

    hill_avg = 0
    sa_avg = 0
    for x in range(1000):
        # Formulate a problem with a 2D hill function and a single maximum value.
        maximum = 30
        initial = randrange(0, maximum)
        p = SineVariant(initial, maximum, delta=1.0)
        # print('Initial                      x: ' + str(p.initial)
        #     + '\t\tvalue: ' + str(p.value(initial))
        #     )

        # Solve the problem using hill-climbing.
        hill_solution = hill_climbing(p)
        # print('Hill-climbing solution       x: ' + str(hill_solution)
        #     + '\tvalue: ' + str(p.value(hill_solution))
        #     )
        hill_avg += p.value(hill_solution)

        # Solve the problem using simulated annealing.
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
        # print('Simulated annealing solution x: ' + str(annealing_solution)
        #     + '\tvalue: ' + str(p.value(annealing_solution))
        #     )
        sa_avg += p.value(annealing_solution)
    print('Hill-climbing average solution over 1000 attempts:\t', hill_avg/1000)
    print('Simulated annealing average solution over 1000 attempts:\t', sa_avg/1000)