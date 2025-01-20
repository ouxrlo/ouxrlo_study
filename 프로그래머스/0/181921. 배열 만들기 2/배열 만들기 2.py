def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if all(i in '05' for i in str(num)):
            answer.append(num)
    return answer if answer else [-1]
