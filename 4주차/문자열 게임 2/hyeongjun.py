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
        s = '' # 계산용 문자열
        for j in range(i, length):
            s += w[j]
            if i < j and s.count(w[i]) == k: # 같은 문자고 인덱스가 더 뒤면
                result.append(len(s))

    while i < length:
        s = ''
        
    if result:
        return min(result)
    else:
        return -1

def find_long(w):
    length = len(w)
    result = []

    for i in range(length):
        s = ''
        for j in range(i, length):
            s += w[j]
            if w[i] == w[j] and i < j and s.count(w[i]) == k:
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