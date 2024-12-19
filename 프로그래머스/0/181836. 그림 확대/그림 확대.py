def solution(picture, k):
    answer = []

    for line in picture:
        for _ in range(k):
            answer.append(''.join([x * k for x in line]))

    return answer
