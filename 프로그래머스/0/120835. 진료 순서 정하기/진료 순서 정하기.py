def solution(emergency):
    # 모든 입력을 정수형으로 변환
    emergency = [int(i) for i in emergency]
    
    answer = []
    
    
    sorted_em = sorted(emergency, reverse=True)
    
    for i in emergency:
        rank = sorted_em.index(i) + 1
        answer.append(rank)
    
    return answer
