def solution(myString, pat):
    
    change = myString.replace("A","X").replace("B","A").replace("X","B")
    
    if pat in change:
        return 1
    else:
        return 0
        