def solution(my_string):
    result = [] 
    for char in my_string:  
        if char not in result:  # 현재 문자가 결과에 없다면
            result.append(char)  # 결과 추가
    return ''.join(result)  # 리스트 -> 문자열 변환하여 반환
