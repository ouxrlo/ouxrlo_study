def solution(name, yearning, photo):
    y_dict ={name[i]:yearning[i] for i in range(len(name))}
    
    answer =[]
    
    for group in photo:
        score = 0
        for j in group:
            score += y_dict.get(j,0)
        answer.append(score)
        
    return answer
