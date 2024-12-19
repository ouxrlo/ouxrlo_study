def solution(my_string, is_suffix):
    suf=len(is_suffix)
    
    if my_string[-suf:]== is_suffix:
        return 1
    else:
        return 0
    
    return answer