def solution(array):
    num = 0 # 많이 나타난 아이 두둥장 횟수
    data = 0 # 최빈값
    for i in set(array):
        if array.count(i) > num:
            num = array.count(i)
            data = i
        elif array.count(i) == num:
            data = -1
    return data