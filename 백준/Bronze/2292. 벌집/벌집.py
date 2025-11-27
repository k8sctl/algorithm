import sys

input = sys.stdin.readline

N = int(input())

layer = 1 # 현재 층
end = 1 # 현재 층의 마지막 방번호

while N > end:
    end += 6 * layer
    layer += 1
    
print(layer)