def solution(start_num, end_num):
    answer = []
    # start_num, end_num 얘넨 정수 내가 만들어야하는건 리스트
    while start_num >= end_num:
        answer.append(start_num)
        start_num -= 1
        
    return answer