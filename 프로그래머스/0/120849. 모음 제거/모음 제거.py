def solution(my_string):
    return "".join([x for x in my_string if not(x in "aeiou")])
