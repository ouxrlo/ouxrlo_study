# carry_time 함수: 주어진 시간(mid) 동안 a, b만큼의 물건을 운반할 수 있는지 확인하는 함수
def carry_time(mid, a, b, g, s, w, t):
    # total_a: a를 운반할 수 있는 양
    # total_b: b를 운반할 수 있는 양
    # total_sum: a와 b를 합친 총 운반 가능한 양
    total_a, total_b, total_sum = 0, 0, 0

    # g, s, w, t는 각각 (g[i], s[i], w[i], t[i])로 각 트럭의 특성을 나타냄
    for i in range(len(g)):
        # max_trips: 한 트럭이 주어진 시간(mid) 동안 할 수 있는 최대 여행 횟수
        max_trips = mid // (2 * t[i])  # 왕복 시간 t[i]에 따라 최대 횟수 계산
        # trip: 현재 시간(mid)에서 짝수 번째 혹은 홀수 번째 여행인지 판단
        trip = (mid // t[i]) % 2

        # max_a: i번째 트럭으로 운반 가능한 a의 양
        max_a = min(g[i], (max_trips * w[i]) + (trip * w[i]))
        # max_b: i번째 트럭으로 운반 가능한 b의 양
        max_b = min(s[i], (max_trips * w[i]) + (trip * w[i]))
        # max_sum: i번째 트럭으로 운반 가능한 a와 b의 합
        max_sum = min(g[i] + s[i], (max_trips * w[i]) + (trip * w[i]))

        # 총 운반 가능한 양 업데이트
        total_a += max_a
        total_b += max_b
        total_sum += max_sum

    # a 이상, b 이상, a와 b 합 이상을 모두 만족하는지 확인
    return total_a >= a and total_b >= b and total_sum >= (a + b)

# solution 함수: 주어진 a, b만큼의 물건을 주어진 시간 내에 운반할 수 있는 최소 시간을 찾는 함수
def solution(a, b, g, s, w, t):
    # 이진 탐색의 범위 설정
    low, high = 0, (10**15)  # 충분히 큰 시간 범위 설정
    answer = high  # 결과를 담을 변수

    # 이진 탐색으로 최소 시간을 찾음
    while low < high:
        mid = (low + high) // 2  # 현재 시간을 중간값으로 설정
        # carry_time 함수로 mid 시간에 a, b를 운반할 수 있는지 확인
        if carry_time(mid, a, b, g, s, w, t):
            high = mid  # 운반 가능하면 시간을 줄여서 최소 시간을 찾음
            answer = min(answer, mid)  # 최솟값 업데이트
        else:
            low = mid + 1  # 운반 불가능하면 시간을 늘림

    return answer  # 최소 시간을 반환


'''
1. carry_time = 주어진 시간(mid) 동안 주어진 트럭들이 운반할 수 있는 전체 양을 계산
2. 이 양이 목표인 a와 b를 각각 옮길 수 있는지
3. solution 함수 = 이진 탐색을 이용해 최소 시간 찾음 (이 문제로 이진탐색 이해)
4. 이진 탐색의 범위 매우 큰 시간까지 설정하여 (10^15) 
5. low와 high 값을 점차 좁혀가며 최적의 최소 시간 찾아봄
6. 주어진 시간 내에 a, b 운반할 수 있는 최소 시간 반환

'''







