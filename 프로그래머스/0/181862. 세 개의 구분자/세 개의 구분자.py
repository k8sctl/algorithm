def solution(myStr):
    answer = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ')
    answer = answer.split()
    
    if not answer:
        answer.append('EMPTY')
    
    return answer