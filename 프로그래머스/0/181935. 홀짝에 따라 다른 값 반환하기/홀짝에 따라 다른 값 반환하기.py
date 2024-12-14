def solution(n):
    answer = 0
    
    if n % 2 == 1: # n이 홀수 일때
        answer = sum(range(1, n+1,2))
    else:
        answer = sum(x**2 for x in range(2, n+1, 2))
        # x**2 for x in range()로 생성된 짝수들에 대해 각각 제곱한 후 그 합을 구하는 코드
    return answer