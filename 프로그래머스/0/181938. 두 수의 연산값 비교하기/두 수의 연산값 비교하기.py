def solution(a, b):
    ab = int(str(a)+str(b)) # 문자열을 숫자열로 바꾸기(숫자열 = 문자열로 더해서 묶어줌)
    
    if ab>2*a*b:
        return ab # int, str 등의 함수는 return으로 출력
    elif ab<2*a*b:
        return 2*a*b
    else:
        return ab