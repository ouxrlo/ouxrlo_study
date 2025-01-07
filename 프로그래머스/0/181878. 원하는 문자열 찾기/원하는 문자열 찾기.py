def solution(myString, pat):
    myString = myString.lower() # lower() 소문자로 바꿔주는 것
    pat = pat.lower()
    
    if pat in myString:
        return 1
    else:
        return 0