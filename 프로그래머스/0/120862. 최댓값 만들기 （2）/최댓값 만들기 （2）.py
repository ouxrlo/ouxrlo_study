def solution(numbers):
    numbers.sort()
    
    answer = max(numbers[0]*numbers[1],numbers[-1]*numbers[-2])
    
    # 가장 작은수 , 가장 큰 수
    return answer