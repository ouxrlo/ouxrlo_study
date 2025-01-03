def solution(a, b):
    return sum(x*y for x,y in zip (a,b) )
# zip 함수는 두 개 이상의 리스트를 병렬로 묶어주는 역할
# 쉽게 생각하면 행-> 열, 열-> 행 바꿔주는 것으로 생각