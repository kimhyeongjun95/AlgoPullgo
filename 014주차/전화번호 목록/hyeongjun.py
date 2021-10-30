# 백준 5052 전화번호 목록

import sys
input = sys.stdin.readline

def phonebook():
    pass
    for i in range(len(numbers)-1):
        length = len(numbers[i])
        if numbers[i] in numbers[i+1][0:length]:
            return 'NO'
    return 'YES'

# set으로 풀어보자
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    numbers = []
    for _ in range(n):
        numbers.append(input().strip())
    numbers.sort() # 길이가 아닌 숫자 순으로 정렬 -> 왼쪽에 있는게 오른쪽에 있는지 확인
    answer = phonebook()
    print(answer)
    