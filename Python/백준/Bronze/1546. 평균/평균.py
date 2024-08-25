# 첫째 줄에는 과목의 개수 N, 둘째 줄에는 N개의 성적들이 주어진다.
# 성적들 중에서 최댓값을 고르고 이 값을 M이라고 한다.
# 그리고 모든 점수들을 ‘점수/M*100’ 식으로 계산하여 새로운 점수를 구한다.
# 새롭게 구한 점수들을 이용해서 새로운 평균을 구하는 프로그램 작성

N = int(input())
scores = list(map(int, input().split()))
    
M = max(scores)

new_scores = []
for i in scores:
    num = (i / M) * 100
    new_scores.append(num) 

avg = sum(new_scores)/len(new_scores)    
print(avg)