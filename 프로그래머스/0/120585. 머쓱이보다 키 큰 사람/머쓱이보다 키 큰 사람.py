def solution(a, h):
    answer = 0
    for x in a:
        if x > h:
            answer += 1
    return answer