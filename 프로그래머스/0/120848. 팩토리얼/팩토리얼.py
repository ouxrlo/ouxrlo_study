def solution(n):
    answer = 0  # 가장 큰 i를 저장할 변수
    fact = 1    # fact를 1로 초기화 (1! = 1)
    i = 1       # i는 1부터 시작
    
    # n보다 큰 팩토리얼을 찾을 때까지 반복
    while fact <= n:
        answer = i  
        i += 1      
        fact *= i   
    
    return answer 
