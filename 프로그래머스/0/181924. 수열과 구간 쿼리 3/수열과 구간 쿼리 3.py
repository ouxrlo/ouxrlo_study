def solution(arr, queries):
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]  # i와 j의 값을 교환
    return arr