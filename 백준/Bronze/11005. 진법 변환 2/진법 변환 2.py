import sys

input = sys.stdin.readline

N, B = map(int, input().split())

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if N == 0:
    print("0")
else:
    result = []
    while N > 0:
        r = N % B            
        result.append(digits[r])
        N //= B              

    result.reverse()
    print("".join(result))