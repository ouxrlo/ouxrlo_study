def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i]:
            answer.extend([arr[i]] * (arr[i] * 2))
        else:
            for _ in range(arr[i]):  # arr[i]번 pop 실행
                answer.pop()
            
    return answer