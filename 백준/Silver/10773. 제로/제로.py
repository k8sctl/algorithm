import sys

n = int(sys.stdin.readline())
ledger = []
answer = 0

for _ in range(n):
    value = int(sys.stdin.readline())
    if value == 0: ledger.pop()
    else: ledger.append(value)
        
for i in ledger:
    answer += i
    
print(answer)