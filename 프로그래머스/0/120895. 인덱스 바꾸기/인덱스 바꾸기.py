def solution(my_string, num1, num2):
    # 문자열 수정 불가능 -> 리스트로 바꿔줘야함.
    char_list = list(my_string)
    
    # 문자열을 바꿔줘야함
    char_list[num1], char_list[num2] = char_list[num2], char_list[num1]
    
    # join() 사용 후 , 리스트를 다시 문자열로 바꿔줌
    result = ''.join(char_list)
    
    return result
