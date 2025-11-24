import sys

input = sys.stdin.readline

N = int(input())

nums = []

for _ in range(N):
    n = int(input())
    nums.append(n)
    
nums.sort()

for i in nums:
    print(i)