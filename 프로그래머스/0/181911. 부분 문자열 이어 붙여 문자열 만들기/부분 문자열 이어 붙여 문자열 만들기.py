def solution(my_strings, parts):
    answer = []
    for i in range(len(my_strings)):
        answer.append(my_strings[i][parts[i][0]:parts[i][1]+1])
        # parts[i][0] 시작인덱스 parts[i][1]+1 끝 인덱스
    return ''.join(answer)