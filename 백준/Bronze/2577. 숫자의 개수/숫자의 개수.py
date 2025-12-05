import sys
input = sys.stdin.readline

nums = [0] * 3
counts = [0] * 10

for i in range(3):
    nums[i] = int(input())

def multiply(arr):
    ans = 1
    for n in arr:
        if n == 0:
            return 0
        ans *= n
    return ans

ans = str(multiply(nums))

for i in ans:
    counts[int(i)] += 1

for i in counts:
    print(i)