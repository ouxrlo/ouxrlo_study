def solution(slice, n):
    total_slices = n
    answer = (total_slices + slice - 1) // slice
    
    return answer