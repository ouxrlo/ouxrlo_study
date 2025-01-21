def solution(i, j, k):
    answer = 0
    for n in range(i, j+1):
        answer += str(n).count(str(k)) # n을 문자열로 변환하고 k의 개수를 더함
    return answer