'''
This module implements a Bayesian network for Thrun's two cancer test
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
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.90, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.90, F: 0.2})
    ])

# P(Cancer | positive results from both tests)
# x * <P(cancer | positive on test1 ^ positive on test2) * P(cancer), P(!cancer | positive on test1 ^ positive on test2) * P(!cancer)>
# x * <P(cancer | positive test1) * P(cancer | positive test2) * P(cancer), P(!cancer | positive test1) * P(!cancer | positive test2) * P(!cancer)>
# x * <(.9 * .9 * .01), (.2 * .2 * .99)>
# x * <.0081, .0396>
# <.0081/.0477, .0396/.0477>
# <.1698, .8302>
print("P(Cancer | positive results from both tests):")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
# P(Cancer | positive on test1, negative on test2)
# x * <P(cancer | positive test1) * P(cancer | negative test2) * P(cancer), P(!cancer | positive test1) * P(!cancer | negative test2) * P(!cancer)>
# x * <(.9 * .1 * .01), (.2 * .9 * .99)>
# x * <.0009, .1782>
# <.0009/.1791, .1782/.1791>
# <.0050, .9950>
print("P(Cancer | positive Test1, negative Test2):")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

# These answers do make sense. Having one test come back negative drastically decreases the probability of having cancer.