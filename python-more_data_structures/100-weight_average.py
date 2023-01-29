#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return(0)
    score_list = [(x * y) for x, y in my_list]
    weight_list = [(y) for x, y in my_list]
    
    total_score = 0
    for i in range(0, len(score_list)):
        total_score = total_score + score_list[i]
    
    total_weight = 0
    for j in range(0, len (weight_list)):
        total_weight = total_weight + weight_list[j]
    
    return(total_score / total_weight)
