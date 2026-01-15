import sys
input = sys.stdin.readline

N, M = map(int, input().split())

used = [False] * (N + 1)
path = []
out = []

def dfs(depth: int):
    if depth == M:
        out.append(" ".join(map(str, path)))
        return

    for i in range(1, N + 1):
        if not used[i]:
            used[i] = True
            path.append(i)

            dfs(depth + 1)

            path.pop()
            used[i] = False

dfs(0)
sys.stdout.write("\n".join(out))