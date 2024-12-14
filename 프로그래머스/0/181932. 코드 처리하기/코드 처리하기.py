def solution(code):
    answer = ''
    mode = 0
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] == '1':  # 비교 연산자 '==' 사용
                mode = 1
            else:
                if idx % 2 == 0:  
                    answer += code[idx]
        else:
            if code[idx] == '1':  # 비교 연산자 '==' 사용
                mode = 0
            else:
                if idx % 2 != 0:  
                    answer += code[idx]

    if answer == "":
        return "EMPTY" 
    else:
        return answer
