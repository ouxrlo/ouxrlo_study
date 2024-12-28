def solution(n, k):
    answer = []
    for i in range(1,n+1): # 1부터 n까지 배열 만들어주고
        if i % k == 0: # 배수는 딱 나눠 떨어지는 수임
            answer.append(i) # append 함수로 데이터 추가
    return answer