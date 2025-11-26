import sys

input = sys.stdin.readline

N = int(input())

line = list(map(int, input().split()))

stack = []
cur = 1

for x in line:
    stack.append(x)
    
    while stack and stack[-1] == cur:
        stack.pop()
        cur += 1
        
if cur == N+1:
    print('Nice')
else:
    print('Sad')