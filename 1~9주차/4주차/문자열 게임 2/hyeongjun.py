# 2
# superaquatornado
# 2
# abcdefghijklmnopqrstuvwxyz
# 5

# aqua; 4 , raquator; 8
# aqua -> a가 2개
# raquator -> r이 2개이면서 가장 긴 문자 / uperaqu는 7개라 안됨
import sys
input = sys.stdin.readline

def find_short(w):
    length  = len(w)
    result = []
    
    for i in range(length):
        s = w[i] # 계산용 문자열
        for j in range(i+1, length):
            s += w[j]
            if s.count(w[i]) == k: # 같은 문자고
                result.append(len(s))
        
    if result:
        return min(result)
    else:
        return -1

def find_long(w):
    length = len(w)
    result = []

    for i in range(length):
        s = w[i]
        for j in range(i+1, length):
            s += w[j]
            if w[i] == w[j] and s.count(w[i]) == k:
                result.append(len(s))
    if result:
        return max(result)
    else:
        return -1

''''''''''''''''''''''''''''''''''''''
t = int(input())

for _ in range(t):
    w = input()
    k = int(input())

    num1 = find_short(w)
    num2 = find_long(w)
    
    if num1 == -1 or num2 == -1:
        print(-1)
    else:
        print(num1, num2)