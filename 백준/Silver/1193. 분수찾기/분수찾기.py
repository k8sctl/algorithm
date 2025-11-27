import sys

X = int(sys.stdin.readline().strip())

line = 0
while line * (line + 1) // 2 < X:
    line += 1

prev_sum = (line - 1) * line // 2   
pos = X - prev_sum                  

if line % 2 == 0:           
    numerator = pos
    denominator = line - (pos - 1)
else:                     
    numerator = line - (pos - 1)
    denominator = pos

print(f"{numerator}/{denominator}")