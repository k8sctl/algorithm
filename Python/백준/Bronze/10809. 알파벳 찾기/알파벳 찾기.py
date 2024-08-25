# 소문자로만 이루어진 단어 S가 주어진다.
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 
# 처음 등장하는 위치를 공백으로 구분해서 출력한다.
# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 
# 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

import string

S = input().strip()
eng = list(string.ascii_lowercase)

answer = []

for char in eng:
    if char in S:
        index = S.index(char)
        answer.append(index)
    else:
        answer.append(-1)  
        
print(*answer)