import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque(range(1, N + 1))
ans = []

while queue:
    queue.rotate(-(K - 1))
    ans.append(str(queue.popleft()))

print("<" + ", ".join(ans) + ">")