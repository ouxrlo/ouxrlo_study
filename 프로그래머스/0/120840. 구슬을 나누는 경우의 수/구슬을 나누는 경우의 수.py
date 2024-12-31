def solution(balls, share):
    # 팩토리얼 함수 정의
    def factorial(n):
        result = 1  
        for i in range(1, n + 1):  
            result *= i
        return result

    # 이부분 지피티 한테 무러봄
    def combination(b, s):
        return factorial(b) // (factorial(s) * factorial(b - s))

    return combination(balls, share)
