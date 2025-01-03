def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        divisor_count = 0 # 약수 개수 초기화

        for j in range(1, i + 1):
            if i % j == 0: # 나누어 떨어지는 경우 약수
                divisor_count += 1 
        
        if divisor_count % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer


# 2

4
5
6
7
8
9
10
11
12
13
import math

def solution(left, right):
    answer = 0
    for i in range(left, right + 1, 1):
        sqrt = math.sqrt(i)
        if int(sqrt) == sqrt:
            answer -= i
        else:
            answer += i

    return answer
