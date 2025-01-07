def solution(my_string, s, e):
    start = my_string[:s] # 시작부분
    center = my_string[s:e+1][::-1]# 중간부분
    end = my_string[e+1:] # 끝부분
    
    answer = start + center + end
    return answer