def solution(strArr):
    answer = []  # 결과를 담을 빈 리스트
    for i, char in enumerate(strArr):  # enumerate를 사용해 인덱스와 문자열을 동시에 처리
        if i % 2 == 0:  # 짝수 인덱스
            answer.append(char.lower())  # 소문자로 변환해서 추가
        else:  # 홀수 인덱스
            answer.append(char.upper())  # 대문자로 변환해서 추가
    return answer
