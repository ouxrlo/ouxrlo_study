def solution(my_string, is_prefix):
    answer = 0
    # 접두사 - 문자열의 처음 부분
    ip=len(is_prefix)
    # my_string의 처음부터 is_prefix 길이만큼 자른 부분이 is_prefix와 같은지 확인합니다.
    if my_string[:ip] == is_prefix:
        return 1
    else:
        return 0
    return answer