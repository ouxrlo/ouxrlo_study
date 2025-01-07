def solution(myString):
    
    p = myString.split("x") # 자른 부분
    l = [len(p) for p in p] # 각 부분 문자열 길이
    
    return l