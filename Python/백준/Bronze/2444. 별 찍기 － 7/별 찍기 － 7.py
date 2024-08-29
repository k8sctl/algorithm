n = int(input())

# 첫 번째 피라미드 부분 (1부터 n까지)
for N in range(n):
    N = N + 1
    print(" " * (n - N), end="")
    print("*" * (2 * N - 1))

# 두 번째 피라미드 부분 (n-1부터 1까지 역순으로)
for N in reversed(range(1, n)):
    print(" " * (n - N), end="")
    print("*" * (2 * N - 1))