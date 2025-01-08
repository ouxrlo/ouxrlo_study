def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        row = bin(arr1[i] | arr2[i])[2:].zfill(n)
        secret_row = ''.join('#' if x == '1' else ' 'for x in row )
        answer.append(secret_row)
        
    return answer
        