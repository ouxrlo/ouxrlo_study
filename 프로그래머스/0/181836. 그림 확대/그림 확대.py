def solution(picture, k):
    answer = []
    
# 가로로 먼저 k배 늘려주기

    for row in picture:
        increase_row =''.join([ch*k for ch in row]) #join과 리스트 컴프리헨션 사용
    
        for x in range(k): # 이미 가로로 k배 늘려진 상태
            answer.append(increase_row) # 세로로 늘려주면 가로x세로 k배 늘리기 성공적
        
    return answer