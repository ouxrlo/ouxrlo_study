def solution(my_string):
    answer = []
    answer = [my_string[i:]for i in range(len(my_string))]
    answer.sort()
    return answer