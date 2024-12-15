def solution(myString):
    answer = ''
    for char in myString:
        if char == 'a':  # a가 나오면 A로 변환
            answer += 'A'
        elif char.isupper() and char != 'A':# 대문자 여부 확인
            answer += char.lower() # 소문자로 변환
        else:
            answer += char #다른건 그대로
    return answer