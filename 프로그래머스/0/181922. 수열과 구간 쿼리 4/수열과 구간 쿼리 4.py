def solution(arr, queries):
    for s,e,k in queries: # 각 쿼리의 배수 가져옴
        for i in range(s,e+1): # s-e 까지 반복
            if i % k == 0:
                arr[i] += 1
            
    return arr