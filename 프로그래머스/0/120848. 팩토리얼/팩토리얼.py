def solution(n):
    # 팩토리얼 함수 정의
    def factorial(i):
        
        if i == 1:
            return 1  # 1을 반환하면 더이상 호출하지 않음
        
        # i * (i-1)!을 계산
        return i * factorial(i - 1) 

    i = 1 
    while True: 
        
        # 만약 i!이 n보다 크면 반복문을 멈춤
        if factorial(i) > n:  
            
            # i! > n 반복 종료
            break
            
         # i를 하나씩 증가하면서 계속 팩토리얼 계산    
        i += 1 

    # i가 한 번 증가 => 그 직전 값인 i-1을 반환
    return i - 1 
