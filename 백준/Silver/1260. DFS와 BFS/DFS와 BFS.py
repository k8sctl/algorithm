import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for nv in graph[v]:
        if not visited[nv]:
            dfs(nv)

def bfs(start):
    visited = [False] * (N + 1)
    q = deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for nv in graph[cur]:
            if not visited[nv]:
                visited[nv] = True
                q.append(nv)

dfs(V)
print()
bfs(V)