def solution(n):
    answer = 0
    nums = []
    
    for i in range(n-1):
        nums.append(i+1)
    
    for j in nums:
        if n % j == 1:
            answer = j
            return answer