N = int(input())
words = []
answers = []

for _ in range(N):
    words.append(input())
    
for i in words:
    answers.append(i[0] + i[-1])

for j in answers:
    print(j, end='\n')