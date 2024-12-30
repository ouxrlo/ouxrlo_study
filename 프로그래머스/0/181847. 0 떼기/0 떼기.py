def solution(n_str):
    idx = 0 # idx 변수 초기화
    for i in range(len(n_str)):
        if n_str [i] == '0': # 0이 아닌 수 나타날때까지 반복
            idx += 1 #
        else:
            break
    return n_str[idx:]