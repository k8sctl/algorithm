def solution(arr, queries):
    
    for i in queries:
        s, e = i
    
        for j in range(s, e+1):
            arr[j] += 1
    
    return arr