def solution(p, m, c):
    total_cost= 0
    for n in range(1, c+1):
        total_cost += p * n
        short_cost = total_cost - m
    return max(short_cost, 0)
            