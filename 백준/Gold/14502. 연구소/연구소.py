import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

empty = []
virus = []

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))
            
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def simulate(walls):
    tmp = [row[:] for row in lab]
    
    for x, y in walls:
        tmp[x][y] = 1
        
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                q.append((nx, ny))
                
    safe = 0
    for i in range(N):
        safe += tmp[i].count(0)
    return safe

ans = 0
for walls in combinations(empty, 3):
    ans = max(ans, simulate(walls))
    
print(ans)