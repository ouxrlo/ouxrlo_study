def solution(rsp):
    answer = ''
    for i in range(len(rsp)):
        if rsp[i] == '2':
            answer += '0' 
        elif rsp[i] == '0':
            answer += '5'
        elif rsp[i] == '5':
            answer += '2'
            
    return answer
            
def solution(rsp):
    d ={'0':'5','2':'0','5':'2'}
    return ''.join(d[i]for i in rsp)
    
        
    