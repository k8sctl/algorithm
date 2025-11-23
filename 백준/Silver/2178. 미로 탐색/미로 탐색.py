import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(N)]

dist = [[0] * M for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0))
    dist[0][0] = 1 

    while queue:
        y, x = queue.popleft()

        if y == N-1 and x == M-1:
            return dist[y][x]
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0<= nx < M:
                if maze[ny][nx] == 1 and dist[ny][nx] == 0:
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((ny, nx))

print(bfs())