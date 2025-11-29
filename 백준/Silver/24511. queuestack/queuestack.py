import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 1) 큐(A[i] == 0)인 자료구조들에 들어 있던 값들만 모음
q = deque()
for i in range(N):
    if A[i] == 0:
        q.append(B[i])

M = int(input())
C = list(map(int, input().split()))

# 2) C의 값들을 앞쪽에 넣고, 뒤에서 뽑아서 출력
ans = []
for x in C:
    q.appendleft(x)       # 새 값은 앞에 넣고
    ans.append(str(q.pop()))  # 맨 뒤 값이 이번에 나가는 값

print(' '.join(ans))