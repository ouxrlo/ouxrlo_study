def solution(num_list):
    odd_numbers = ""
    even_numbers = ""
    
    for num in num_list:
        if num % 2 == 0:  # 짝수인 경우
            even_numbers += str(num)
        else:  # 홀수인 경우
            odd_numbers += str(num)
            
    if odd_numbers:  # 홀수 문자열이 비어있지 않으면 변환
        odd_number_int = int(odd_numbers)
    else:  # 홀수 문자열이 비어있으면 0으로 처리
        odd_number_int = 0
        
    if even_numbers:  # 짝수 문자열이 비어있지 않으면 변환
        even_number_int = int(even_numbers)
    else:  # 짝수 문자열이 비어있으면 0으로 처리
        even_number_int = 0
    
    # 두 정수의 합을 반환
    answer = odd_number_int + even_number_int
        
    return answer