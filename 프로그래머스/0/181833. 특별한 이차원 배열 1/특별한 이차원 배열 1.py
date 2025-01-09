# 1
def solution(n):
    answer = []
    for i in range(n):
        row = []
        for j in range(n):
            if i ==j:
                row.append(1)
            else:
                row.append(0)
        answer.append(row)
            
    return answer
    
    
# 2
def solution(n):
    return [[int(i==j)for i in range(n)]for j in range(n)]



# 3
def solution(n):
    answer = []
    for i in range(n):
        arr = [0] * n
        arr[i] = 1
        answer.append(arr)
        
    return answer