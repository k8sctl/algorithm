import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [ [] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, N+1):
    graph[i].sort()
    
visited = [0] * (N+1)
order = 1

def dfs(cur_v):
    global order
    visited[cur_v] = order
    order += 1
    
    for v in graph[cur_v]:
        if visited[v] == 0:
            dfs(v)
            
dfs(R)

for i in range(1, N+1):
    print(visited[i])