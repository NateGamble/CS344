'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@editor: Nate Gamble
@version February 28, 2019
'''

import sys
sys.path.append('cs344-code/tools/aima')
from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print("P(Cavity|toothache):\t", PC.show_approx())

# P(Cavity|Catch=T)
    # P(Cavity=T|Catch=T) = P(Cavity=T and Catch=T) / P(Catch=T) 
    # = .180 / .340 = 53.9%
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print("P(Cavity|catch):\t", PC.show_approx())

H, T = True, False
P = JointProbDist(['Coin1', 'Coin2'])
P[H, H] = 0.25; P[H, T] = 0.25
P[T, H] = 0.25; P[T, T] = 0.25

PC = enumerate_joint_ask('Coin2', {'Coin1': H}, P)
print("P(Coin2|Coin1=heads):\t", PC.show_approx())
