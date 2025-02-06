def solution(spell, dic):
    spell_set = set(spell)  
    for i in dic:
        if spell_set == set(i) and len(spell) == len(i):
            return 1
    return 2
