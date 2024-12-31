# 1
def solution(balls, share):
    def factorial(n):
        result = 1  
        for i in range(1, n + 1): 
            result *= i
        return result

    def combination(b, s):
        return factorial(b) // (factorial(s) * factorial(b - s))

    return combination(balls, share)

# 위와 같이 풀었는데 너무 길어 줄일수 없나 생각해보다가 아래와 같이 정리해봤더니 훨씬 깔꼼

from math import factorial as f

def solution(balls, share):
    return f(b) // f(s) // f(b - s)

# 2

import math


def solution(balls, share):
    return math.comb(balls, share)

