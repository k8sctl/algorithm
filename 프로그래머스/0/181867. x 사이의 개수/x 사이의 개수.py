def solution(myString):
    answer = []
    count = 0
    l = list(myString.split("x"))
    
    for i in l:
        count = 0
        for _ in i:
            count += 1
        answer.append(count)
        
    return answer