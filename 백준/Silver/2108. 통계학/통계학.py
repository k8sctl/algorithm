import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().strip())
arr = [int(input().strip()) for _ in range(n)]
arr.sort()

# 1) 산술평균
mean = sum(arr) / n
avg = int(mean + 0.5) if mean >= 0 else int(mean - 0.5)

# 2) 중앙값
median = arr[n // 2]

# 3) 최빈값 (여러 개면 두 번째로 작은 값)
cnt = Counter(arr)
max_freq = max(cnt.values())
modes = [k for k, v in cnt.items() if v == max_freq]
modes.sort()
mode = modes[1] if len(modes) >= 2 else modes[0]

# 4) 범위
range_val = arr[-1] - arr[0]

print(avg)
print(median)
print(mode)
print(range_val)