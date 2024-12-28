def solution(arr, n):
    answer = []  

    if len(arr) % 2 == 1:  # 배열의 길이가 홀수라면
        for i in range(len(arr)):  # 배열의 모든 인덱스를 순회
            if i % 2 == 0:  # 짝수 인덱스라면
                answer.append(arr[i] + n)  # n을 더한 값을 추가합니다.
            else:  # 홀수 인덱스라면
                answer.append(arr[i])  # 원래 값을 그대로 추가합니다.
    else:  # 배열의 길이가 짝수라면
        for i in range(len(arr)):  # 배열의 모든 인덱스를 순회합니다.
            if i % 2 == 1:  # 홀수 인덱스라면
                answer.append(arr[i] + n)  # n을 더한 값을 추가합니다.
            else:  # 짝수 인덱스라면
                answer.append(arr[i])  # 원래 값을 그대로 추가합니다.

    return answer 


                