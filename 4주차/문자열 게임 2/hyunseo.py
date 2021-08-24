import sys
from collections import defaultdict

'''
superaquatornado
2
'''

def string_game(string):
    len_str = len(string)

    # K개 이상 있는 문자만 따로 저장
    alpha = defaultdict(list)
   
    for i in range(len_str):
        if string.count(string[i]) >= K:
            alpha[string[i]].append(i)
    # alpha = {'u': [1, 7], 'r': [4, 11], 'a': [5, 8, 13], 'o': [10, 15]}

    # K개 이상 있는 문자가 없다면 -1
    if not alpha:
        return (-1,)
    
    # K개 이상 있는 문자에 대해 문자열 게임 진행
    min_str = 10000
    max_str = 0

    for idx_lst in alpha.values():
        for j in range(len(idx_lst)-K+1):
            temp = idx_lst[j+K-1] - idx_lst[j] + 1

            if temp < min_str:
                min_str = temp

            if temp > max_str:
                max_str  = temp
    
    return min_str, max_str


T = int(sys.stdin.readline())

for t in range(1, T+1):
    string = sys.stdin.readline().strip()
    K = int(sys.stdin.readline())

    print(*string_game(string))