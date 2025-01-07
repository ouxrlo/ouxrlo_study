def solution(myString, pat):
    
    end = myString.rfind(pat)+len(pat) #rfind() 가장 마지막 위치를 반환
    
    answer = myString[:end]
    return answer