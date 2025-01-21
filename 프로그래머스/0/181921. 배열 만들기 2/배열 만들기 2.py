def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if all(i in '05' for i in str(num)):# "05" 모든 자릿수가 '0' 또는 '5'로만 이루어졌는지 확인
            answer.append(num)
    return answer if answer else [-1]

