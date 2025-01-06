def solution(num_list, n):
    for element in num_list:
        if element == n: # element - 리스트의 각 요소
            return 1
    return 0



def solution(num_list, n):
    return int(n in num_list)