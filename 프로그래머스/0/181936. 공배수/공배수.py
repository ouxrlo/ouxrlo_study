def solution(number, n, m):
    if number % n == 0 and number % m == 0 : # n의 배수이면서 m의 배수인지 확인
        answer = 1 # n의 배수이면서 m의 배수일 시, 1
    else:
        answer = 0 # n의 배수이면서 m의 배수가 아닐 시, 0
    return answer # 리턴