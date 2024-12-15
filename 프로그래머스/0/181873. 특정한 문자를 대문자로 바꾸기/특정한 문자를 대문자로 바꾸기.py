def solution(my_string, alp):
    answer = ''
    for i in my_string:
        answer = my_string.replace(alp,alp.upper())
    return answer