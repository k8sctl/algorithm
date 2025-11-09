import math

def solution(progresses, speeds):
    answer = []
    l1 = []
    
    # 남은 작업 일수 계산
    for i in range(0, len(progresses)):
        v1 = 100 - progresses[i]
        v2 = v1 / speeds[i]
        l1.append(math.ceil(v2))
    
    pre_value = l1[0]
    count = 0
    
    for j in l1: 
        if pre_value < j:
            answer.append(count)
            count = 1
            pre_value = j
            
        elif pre_value >= j:
            count += 1
            
    answer.append(count)
    return answer