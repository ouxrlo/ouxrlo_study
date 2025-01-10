def solution(binomial):
    a,op,b = binomial.split()
    a,b = int(a), int(b)
    
    if op == '+':
        answer = a+b
    elif op == '-':
        answer = a-b
    elif op == '*':
        answer = a*b

        
    return answer
# def solution(binomial):
#     return (int(a,b) for i in binomial if a,b>=0 else op)