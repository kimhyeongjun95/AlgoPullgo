import sys

def plus_minus(ans):
    if plus:
        ans += temp
    else:
        ans -= temp
    
    return ans, 0

string = sys.stdin.readline().strip()

answer = 0
temp = 0
plus = True

for i in range(len(string)+1):
    if i == len(string):
        answer, temp = plus_minus(answer)
    elif string[i] == '-':
        answer, temp = plus_minus(answer)
        plus = False
    elif string[i] == '+':
        answer, temp = plus_minus(answer)
    else:
        temp = temp*10 + int(string[i])

print(answer)