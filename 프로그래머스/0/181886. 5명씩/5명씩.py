def solution(names):
    answer = []
    for i in range(0, len(names), 5):
        group = names[i:i+5] # 0-5 그룹 지어줌
        answer.append(group[0])
    return answer
