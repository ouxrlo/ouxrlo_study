def solution(k, d):
    count = 0
    max_a = d // k  # x축 방향으로 가능한 최대 값
    
    for a in range(max_a + 1):  # x 값
        max_b = int((d**2 - (a * k)**2) ** 0.5) // k  # 주어진 x에 대해 가능한 y 값
        count += max_b + 1  # y 값은 0부터 max_b까지 포함

    return count


