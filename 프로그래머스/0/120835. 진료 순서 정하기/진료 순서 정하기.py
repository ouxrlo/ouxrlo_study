def solution(emergency):
    sort = sorted(emergency, reverse=True)
    return [sort.index(i) + 1 for i in emergency]
