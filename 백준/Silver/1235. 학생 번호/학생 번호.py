import sys

input = sys.stdin.readline

N = int(input().strip())
nums = [input().strip() for _ in range(N)]

L = len(nums[0])

for k in range(1, L+1):
    seen = set()
    for s in nums:
        seen.add(s[-k:])
    if len(seen) == N:
        print(k)
        break