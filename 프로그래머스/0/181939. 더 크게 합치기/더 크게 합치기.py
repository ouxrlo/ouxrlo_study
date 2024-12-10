def solution(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    
    if ab > ba:
        return int(ab)
    elif ab < ba:
        return int(ba)
    else:
        return int(ab)