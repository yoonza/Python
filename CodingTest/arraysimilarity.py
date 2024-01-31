def solution(s1, s2):
    set_s1 = set(s1)
    set_s2 = set(s2)
    
    common_set_values = set_s1.intersection(set_s2)
    answer = len(common_set_values)
    
    return answer