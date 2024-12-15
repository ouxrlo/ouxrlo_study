def solution(rny_string):
    answer = ''  # 결과를 저장할 빈 문자열 준비
    for i in rny_string:  # 문자열의 각 글자를 순서대로 확인
        if i == 'm':  # 현재 글자가 'm'이면
            answer += 'rn'  # 'rn'을 추가
        else:  # 현재 글자가 'm'이 아니면
            answer += i  # 해당 글자를 그대로 추가
    return answer  # 최종 결과 반환
