import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    W = input().rstrip()
    K = int(input())
    counter_dict = {}
    result = []
    for char in W:
        counter_dict[char] = W.count(char)
    
    alpha_list = []
    for key, value in counter_dict.items():
        if value >= K:
            alpha_list.append(W.index(key))

           
    