import sys
input = sys.stdin.readline

N = int(input())
d = {}

for _ in range(N):
    name, level = input().split()
    d[name] = int(level)

answer = min(d, key=d.get)
print(answer)