'''
This module implements a Bayesian network for exercise 5.3 - Happiness
It's taken from the AIMA Python code.

@author: Nate Gamble
@version March 6, 2020
'''
import sys
sys.path.append('/home/neg6/cs344/cs344-code/tools/aima')
sys.path.append('D:\\School\\2019-20 Spring\\CS 344 AI\\cs344-code\\tools\\aima')
from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask


# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
happy = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', .01),
    ('Happy', 'Sunny Raise', {(T, T): 1, (T,F): .7, (F,T): .9, (F,F): .1})
    ])

# P(Raise | sunny)
# <.01, .99>
print("P(Raise | sunny):")
print(enumeration_ask('Raise', dict(Sunny=T), happy).show_approx())
# P(Raise | happy ^ sunny)
# x * <P(raise | happy) * P(raise | sunny) * P(raise), P(!raise | happy) * P(!raise | sunny) * P(!raise)>
# x * <(.9 * .01 * .01), (.07 * .99 * .99)>
# x * <.00009, .06861>
# <.00009/.0687, .06861/.0687>
# <.00131, .99869>
print("P(Raise | happy, sunny):")
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), happy).show_approx())


# P(Raise | happy)
print("P(Raise | happy):")
print(enumeration_ask('Raise', dict(Happy=T), happy).show_approx())
# P(Raise | happy ^ !sunny)
print("P(Raise | happy ^ !sunny):")
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())

# The results for 5.3.b don't quite make sense to me. Whether it is sunny or not should not affect the probability of being given a raise,
# as shown in 5.3.a.i where sunniness had no affect on getting a raise