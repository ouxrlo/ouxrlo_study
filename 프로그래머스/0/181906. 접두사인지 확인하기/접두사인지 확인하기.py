def solution(my_string, is_prefix):
    answer = 0
    
    ip=len(is_prefix)
    
    # my_string의 처음부터 is_prefix 길이만큼 자른 부분 = is_prefix 확인
    
    if my_string[:ip] == is_prefix:
        return 1 # 접두사면 1
    else:
        return 0 # 아니면 0
    
    return answer