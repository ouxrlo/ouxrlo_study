def solution(numbers):
    find_numbers = [i for i in range(10) if i not in numbers]
    # 숫자로 리스트 생성 후, 없는 번호를 빼내 합해줌
    answer = sum(find_numbers)
    return answer