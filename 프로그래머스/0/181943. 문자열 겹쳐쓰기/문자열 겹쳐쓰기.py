def solution(my_string, overwrite_string, s):
    front = my_string[:s] # 앞부분 슬라이싱
    middle = overwrite_string # 덮어 쓸 부분
    back = my_string[s+ len(overwrite_string):] #뒷부분 슬라이싱
    
    result = front+ middle+ back # 다 합치기
    return result