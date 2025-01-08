# 1
def solution(rny_string):
    return ''.join(['rn' if i == 'm' else i for i in rny_string])  

# 2
def solution(rny_string):
    return rny_string.replace('m', 'rn')