def solution(s):
    answer = []  
    
    for char in s.split():  
        if char == "Z":  
            if answer: 
                answer.pop()  
        else:
            answer.append(int(char))  #
    
    return sum(answer) 
