import sys

input = sys.stdin.readline

N = int(input())

side = 2 ** N + 1
answer = side * side

print(answer)