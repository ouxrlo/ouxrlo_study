def solution(q, r, code):
    answer = ''
    for index in range(len(code)):
        if index % q == r:
            answer += code[index]
    return answer