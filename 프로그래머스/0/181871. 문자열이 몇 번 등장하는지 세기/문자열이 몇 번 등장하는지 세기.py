def solution(myString, pat):
    answer = 0
    for i in range(len(myString)- len(pat)+1):
        
        part = myString[i:i+len(pat)]
        
        if part == pat:
            answer += 1
    return answer