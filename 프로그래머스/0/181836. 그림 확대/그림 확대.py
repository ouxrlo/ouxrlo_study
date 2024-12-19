def solution(picture, k):
    result = []
    for p in picture:
        s = ''
        for a in p:
            s += a * k
        for i in range(k):
            result.append(s)
    return result
'''
def solution(picture, k):
    answer = []
    
# 저는 먼저 가로로 k배 늘려주겠다요

    for row in picture:
        up =''.join([ch*k for ch in row]) #join과 리스트 컴프리헨션 사용
    
        for x in range(k): # 이미 가로로 k배 불려진 상태다요
            answer.append(up) # 세로로 늘려주면 가로x세로 k배 늘리기 성공적
        
    return answer
    '''