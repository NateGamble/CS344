'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@editor: Nate Gamble
@version March 6, 2020
'''
import sys
sys.path.append('/home/neg6/cs344/cs344-code/tools/aima')
sys.path.append('D:\\School\\2019-20 Spring\\CS 344 AI\\cs344-code\\tools\\aima')
from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask


# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# Compute P(Burglary | John and Mary both call).
print("P(Burglary | John and Mary both call):")
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# elimination_ask() is a dynamic programming version of enumeration_ask().
print("elimination_ask():")
print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
print("gibbs_ask():")
print(gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# See the explanation of the algorithms in AIMA Section 14.4.

## 5.1

#P(Alarm | burglary and not earthquake)
print("P(Alarm | burglary and not earthquake):")
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
#P(John calls | burglary and not earthquake)
print("P(John calls | burglary and not earthquake):")
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())
#P(Burglary | alarm)
print("P(Burglary | alarm):")
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
#P(Burglary | John and mary both call)
print("P(Burglary | John and Mary both call):")
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())


## 5.4
# elimination_ask() gives the same answer as enumeration_ask(), because it is a direct simplification of enumeration_ask().
# elimination_ask() only calculates each variable needed once and stores the result, where enumeration_ask() calculates
# each variable every time it is needed. gibbs_ask() gets a slightly different answer than the other two algorithms.
# This is because gibbs_ask() simplifies the problem so that an estimate can be found quickly. This is very helpful
# with problems that have many variables and causes for each effect.