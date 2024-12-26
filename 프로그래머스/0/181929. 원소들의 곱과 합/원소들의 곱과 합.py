def solution(num_list):
    x = 1
    
    for n in num_list:
        x *= n
        
    p = sum(num_list)**2
    
    return 1 if x<p else 0 