import sys

input = sys.stdin.readline

arr = []
for i in range(8):
    score = int(input())
    arr.append((score, i+1))
    
arr.sort()

top5 = arr[-5:]
score_sum = sum(s for s, idx in top5)
indices = sorted(idx for s, idx in top5)
    
print(score_sum)
print(*indices)