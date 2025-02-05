def solution(s):
    s = s.lower()
    cp = s.count('p')
    cy = s.count('y')
    
    if cp == cy:
        return True
    elif cp != cy:
        return False
    else:
        return True
