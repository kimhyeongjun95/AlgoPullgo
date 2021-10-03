# 백준 1339 단어 수학

# 알파벳 -> 숫자
# 그 수의 합을 최대로 만드는 프로그램

import sys
input = sys.stdin.readline

# 2
# GCF
# ACDEB

# A=9, C=8, D=7, E=5, B=4
#           G=6, C=8, F=3
# 98754 + 683 = 99437

# 자리수가 높은 순으로 높은 숫자
# A: 10000 * 9 = 90000
# C: 1000 * 8 + 10 * 8 = 8080
# D: 100 * 7 = 700
# G: 100 * 6 = 600
# E: 10 * 5 = 50
# B: 1 * 4 = 4
# F: 1 * 3 = 3

import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(input().strip())

dict = {}
for number in numbers: # GCF, ACDEB...
    length = len(number) - 1
    for i in number: # G/C/F , A/C/D/E/B...
        if i not in dict:
            # 10의 2승 = 100, 10의 1승 = 10, 10의 0승 = 1
            dict[i] = pow(10, length) 
        else:
            dict[i] += pow(10, length)

        length -= 1

# sorted는 리스트를 반환
result = sorted(dict.values(), reverse=True)

count = 9
answer = 0
for i in result:
    answer += i * count    
    count -= 1

print(answer)
