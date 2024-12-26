def solution(str_list, ex):
    answer = ""
    for i in str_list:
        if ex in i:
            continue
        answer += i
    return answer
    # return ''.join([i for i in str_list if ex not in i])