# 백준 5052 전화번호 목록
import sys
from collections import defaultdict

input = sys.stdin.readline

def can_cailling(numbers, idx):
    global answer

    temp = defaultdict(list)
    check = []

    for number in numbers:
        if len(number) > idx:
            temp[number[idx]].append(number)

            if len(number) == idx+1:
                check.append(number[idx])

    for key, lst in temp.items():
        if len(lst) > 1:
            if key in check:
                answer = 'NO'
                return

            can_cailling(lst, idx+1)


for _ in range(int(input())):
    N = int(input())
    numbers = [input().strip() for _ in range(N)]

    answer = 'YES'
    can_cailling(numbers, 0)

    print(answer)