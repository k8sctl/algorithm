import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

prime_count = 0

for x in nums:
    if x == 1:
        continue

    is_prime = True
    # 2부터 √x 까지만 검사
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            is_prime = False
            break

    if is_prime:
        prime_count += 1

print(prime_count)