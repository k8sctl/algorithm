# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
# 첫째 줄에는 테스트케이스의 수 T가 입력
# 둘째 줄에는 R과 S가 공백으로 구분되어 입력
# 이렇게 만들어진 새로운 문자열 P를 출력

T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    
    P = ""
    
    for char in S:
        P += (char * R) 

    print(P)