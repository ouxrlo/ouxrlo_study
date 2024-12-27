# 결국 제곱근 구하라는 말이자나ㅡㅡ

# def solution(n):
#     if n**2/n == n:
#         return 1
#     else:
#         return 2
    
# 머리 비우고 보이는데로 적어봤는데 역시 답이 아니래 ㅎ,,
# 그래서 지피티한테 제곱근 구하는 식이 따로 있냐고 물어봄,,,

# import math

# def solution(n):
    
#     sqrt_n = math.sqrt(n) # 얘가 n의 제곱근 식 
    
#     if sqrt_n.is_integer(): # is_integer() 계산 된 제곱근이 정수 인지
#         return 1
#     else:
#         return 2

def solution(n):
    for i in range(1, n // 2):
        if i * i == n:
            return 1
    return 2
    