import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
targets = list(map(int, input().split()))

dq = deque(range(1, N+1))
ans = 0

for x in targets:
    idx = dq.index(x)
    half = len(dq) // 2
    
    if idx <= half:
        dq.rotate(-idx)
        ans += idx
    else:
        r = len(dq) - idx
        dq.rotate(r)
        ans += r
        
    dq.popleft()
    
print(ans)