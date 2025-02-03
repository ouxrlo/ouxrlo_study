def solution(hp):
    k = hp // 5
    a = hp % 5
    
    m = a // 3
    a = a % 3
    
    w= a
    
    return k + m + w
