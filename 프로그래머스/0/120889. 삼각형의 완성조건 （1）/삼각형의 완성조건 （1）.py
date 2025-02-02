def solution(sides):
    long = max(sides)
    some = sum(sides)-max(sides)
    
    if long<some:
        return 1
    else:
        return 2