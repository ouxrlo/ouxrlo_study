def solution(a, d, included):
    answer = 0  
    for i in range(len(included)):
        # (i + 1)번째 항 계산: a + i * d
        current_term = a + i * d
        if included[i]:
            answer += current_term
    return answer
