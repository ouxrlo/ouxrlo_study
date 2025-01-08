def solution(rny_string):
    return ''.join(['rn' if i == 'm' else i for i in rny_string])  
