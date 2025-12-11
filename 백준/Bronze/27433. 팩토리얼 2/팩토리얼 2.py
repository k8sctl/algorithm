import sys

input = sys.stdin.readline

def recursion(n):
    if n == 0 or n == 1:
        return 1
    return n * recursion(n - 1)

n = int(input())
print(recursion(n))