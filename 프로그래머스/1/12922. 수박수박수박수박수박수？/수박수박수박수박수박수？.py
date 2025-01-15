def solution(n):
    pattern = "수박" * (n // 2 + 1)  
    return pattern[:n]  



 # 1. '수박'이라는 패턴을 반복 생성하고 n 길이만큼 잘라서 사용
# n이 짝수든 홀수든 충분히 길게 반복 생성
# n 길이만큼 슬라이싱하여 반환