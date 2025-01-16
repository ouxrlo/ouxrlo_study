def solution(num_list):
    hol = 0
    jjak = 0
    
    for n in num_list:
        if n % 2 == 0:
            jjak += 1
        else:
            hol += 1
    
    return [jjak, hol]