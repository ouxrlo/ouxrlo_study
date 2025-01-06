def solution(num_list, n):
    if not num_list:
        return []
    row = num_list[:n]
    rest = solution(num_list[n:], n)
    return [row]+rest