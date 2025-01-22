def solution(my_string):
    answer = ''
    for x in my_string:
        if x not in "aeiou":  # 모음이 아니면
            answer += x  # answer에 추가
    return answer
        