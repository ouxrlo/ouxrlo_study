# 1

from math import factorial as f

def solution(balls, share):
    return f(balls) // f(share) // f(balls - share)

# 2

import math


def solution(balls, share):
    return math.comb(balls, share)

# 3
