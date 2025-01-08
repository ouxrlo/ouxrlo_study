def solution(arr, intervals):
    f = arr[intervals[0][0]:intervals[0][1]+1]
    s = arr[intervals[1][0]:intervals[1][1]+1]
    answer = f+s
    return answer