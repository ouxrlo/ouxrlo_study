def solution(a, b):
    answer = 0
    for n in range(6):
        if a % 2 == 1 and b % 2 == 1:
            return (a**2) + (b**2)
        elif a % 2 == 1 or b % 2 == 1:
            return 2 * (a+b)
        else:
            return abs(a-b)
    return answer