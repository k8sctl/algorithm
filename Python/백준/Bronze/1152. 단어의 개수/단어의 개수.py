# 문장을 입력 받으면 공백을 기준으로 단어로 분리한다.
# 이렇게 분리했을 때, 단어가 몇개인지 출력

sentence = input()
words = sentence.split()
print(len(words))