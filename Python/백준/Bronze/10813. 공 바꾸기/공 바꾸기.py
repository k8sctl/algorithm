# N개의 바구니 (1번 ~ N번)
# 바구나에는 해당 번호의 공이 들어있음.
# 예시) 1번 바구니에는 1번 공, 2번 바구니에는 2번 공, ... , N번 바구니에는 N번 공
# i와 j를 입력 받고 i번 바구니와 j번 바구니의 공을 서로 바꾼다.
# 해당 작업을 M번 반복한다.
# 첫 번째 줄에는 N과 M이 입력
# 두 번째 줄에는 i와 j가 출력

N, M = map(int, input().split())
basket = [0] * N
change = 0

for n in range(N):
    basket[n] = n+1

for _ in range(M):
    i, j = map(int, input().split())
   
    change = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = change
    
print(*basket)