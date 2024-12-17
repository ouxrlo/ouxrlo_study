def solution(array):
    answer = 0
    from collections import Counter

    # 저는 counter를 딕셔너리로 저장했구만요
    counter = Counter(array)

    # 숫자가 나온것중에 최대값
    max_count = max(counter.values())

    
    if list(counter.values()).count(max_count) > 1:
        return -1  # 최빈값이 여러 개면 -1 반환하구만요
    else:
        # 먹이를 찾으러 다니는 하이에나 처럼 최빈값을 찾아다녀보자구
        for key, value in counter.items():
            if value == max_count:
                answer = key
                break

    return answer

    return answer