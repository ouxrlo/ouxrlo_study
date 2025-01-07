# 문자열의 개수 세어주는 파이썬 표준 라이브러리에 포함된 클래스
from collections import Counter 

def solution(strArr):
    l = [len(str) for str in strArr]
    l_count = Counter(l)
    
    return max(l_count.values())