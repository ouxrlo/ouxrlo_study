def solution(arr):
    n = len(arr) # n*n 배열크기
    for i in range(n):
        for j in range(n):
            # 이거 대칭인지 아닌지 물어보는 것 같아유!!
            if arr[i][j] != arr[j][i]: 
                return 0    # 대칭 아니면 0
    return 1    # 대칭이면 1
    