def solution(picture, k):
    answer = [] # 1.초기화

    for line in picture:  # 각 열을 처리
        for _ in range(k):  # k배 증가
            answer.append(''.join([f * k for f in line]))  # 4.세로로 k배 증가, 7.세로로 k배 증가=> 증가시킨 다음에 빈 문자열에 넣음
                                    # 리스트 -> 3.line = "AB", 가로로 k배 증가 => 빈 문자열에 넣음
                                    # 컴프리헨션 -> 6.line = "CD", 가로로 k배 증가 => 빈 문자열에 넣음
                            
    return answer   # 8. answer 을 리턴

