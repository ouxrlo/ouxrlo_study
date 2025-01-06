# def solution(num_list, n):
#     answer = []
    
#     for i in range(0, len(num_list), n):  
#         answer.append(num_list[i:i + n])  
 
#     return answer

def solution(num_list, n):
    if not num_list:
        return []
        
    row = num_list[:n]
    part = solution(num_list[n:], n)
    return [row]+part