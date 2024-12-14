# 입력 받기
str, n = input().strip().split()
n = int(n)  # 반복 횟수를 정수로 변환

# 제한사항 확인 및 처리
if 1 <= len(str) <= 10 and 1 <= n <= 5:
    print(str * n)  # 문자열 반복 및 출력
else:
    print("제한사항을 만족하지 않습니다.")
