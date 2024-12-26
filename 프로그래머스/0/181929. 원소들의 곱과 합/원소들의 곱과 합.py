def solution(num_list):
    x = 1
    
    for n in num_list:
        x *= n
        
    p = sum(num_list)**2
    
    return 1 if x<p else 0 


# def solution(num_list):
#     sum = 0
#     mul = 1
#     for n in num_list:
#         sum += n
#         mul *= n
#     return int(mul < sum**2)