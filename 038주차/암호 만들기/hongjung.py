import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
moeum = ['a', 'e', 'i', 'o', 'u']
moeum_list = []
not_moeum_list = []
for i in list(map(str, sys.stdin.readline().split())):
    if i in moeum:
        moeum_list.append(i)
    else:
        not_moeum_list.append(i)

answer_list = []
for i in range(1, len(moeum_list) + 1):
    for combi1 in list(combinations(moeum_list, i)):
        for j in range(2, len(not_moeum_list) + 1):
            if i + j == L:
                for combi2 in list(combinations(not_moeum_list, j)):
                    answer = list(combi1 + combi2)
                    answer.sort()
                    answer_list.append("".join(answer))

answer_list.sort()
for a in answer_list:
    print(a)

