# N개의 바구니 (1번 ~ N번)
# M번 순서를 역순으로 바꾼다. (범위를 정해놓고 해당 범위 안에 있는 바구니의 순서를 역순으로 바꾼다.)
# 입력 첫째 줄에는 N과 M이 주어진다.
# 입력 둘째 줄부터는 범위가 주어진다. (i, j : i번째 바구니부터 j번째 바구니까지)

N, M = map(int, input().split())

baskets = []

for n in range(N):
    baskets.append(n+1)

for _ in range(M):
    i, j = map(int, input().split())
    baskets[i-1:j] = baskets[i-1:j][::-1]

print(*baskets)