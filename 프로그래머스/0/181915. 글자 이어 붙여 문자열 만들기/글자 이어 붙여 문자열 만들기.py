def solution(my_string, index_list):
    answer = ''
    for idx in index_list:
        char = my_string[idx] #idx에 해당하는 문자 가져오기
        answer += char
    return answer