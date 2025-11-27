import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())  # M: 가로, N: 세로

board = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
dist = [[-1] * M for _ in range(N)]

# 시작점(익은 토마토) 모두 추가
for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            queue.append((y, x))
            dist[y][x] = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# BFS
while queue:
    y, x = queue.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < M:
            # 안 익은 토마토이고, 아직 방문하지 않은 경우
            if board[ny][nx] == 0 and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                board[ny][nx] = 1
                queue.append((ny, nx))

# 결과 계산
answer = 0

for y in range(N):
    for x in range(M):
        # 토마토가 있는데 끝까지 0이면(안 익은 상태로 남으면) 실패
        if board[y][x] == 0 and dist[y][x] == -1:
            print(-1)
            sys.exit(0)
        if dist[y][x] > answer:
            answer = dist[y][x]

print(answer)