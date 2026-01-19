import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
tmp = [0] * n

count = 0
ans = -1

def merge_sort(p, r):
    global ans
    if ans != -1:  # 이미 답을 찾았으면 더 진행하지 않음
        return
    if p >= r:
        return
    q = (p + r) // 2
    merge_sort(p, q)
    merge_sort(q + 1, r)
    merge(p, q, r)

def merge(p, q, r):
    global count, ans
    if ans != -1:
        return

    i, j, t = p, q + 1, p

    while i <= q and j <= r:
        if a[i] <= a[j]:
            tmp[t] = a[i]
            i += 1
        else:
            tmp[t] = a[j]
            j += 1
        t += 1

    while i <= q:
        tmp[t] = a[i]
        i += 1
        t += 1

    while j <= r:
        tmp[t] = a[j]
        j += 1
        t += 1

    for x in range(p, r + 1):
        a[x] = tmp[x]
        count += 1
        if count == k:
            ans = a[x]
            return

merge_sort(0, n - 1)
print(ans)