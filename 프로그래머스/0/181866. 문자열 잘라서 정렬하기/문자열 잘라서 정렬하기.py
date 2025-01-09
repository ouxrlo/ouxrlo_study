def solution(myString):
    p = myString.split('x')
    
    pd = [i for i in p if i]
    
    answer = sorted(pd)
    
    return answer