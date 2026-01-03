def solution(a, b):
    str_sum = str(a) + str(b)
    int_sum = 2 * a * b
    
    if int(str_sum) > int_sum: 
        return int(str_sum)
    
    else:
        return int_sum