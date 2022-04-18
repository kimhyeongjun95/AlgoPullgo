import sys
from collections import defaultdict

T = int(sys.stdin.readline())

for tc in range(1, T + 1):
    N = int(sys.stdin.readline())
    node_dict = defaultdict(int)
    for _ in range(N - 1):
        A, B = map(int, sys.stdin.readline().split())
        node_dict[B] = A

    child1, child2 = map(int, sys.stdin.readline().split())
    child1_list = [child1]
    while True:
        parent = node_dict[child1]
        if parent == 0:
            break
        child1_list.append(parent)
        child1 = parent
    
    answer = 0
    while True:
        parent = node_dict[child2]
        if parent == 0:
            answer = child1
            break
        elif parent in child1_list:
            answer = parent
            break
        else:
            child2 = parent
            
    print(answer)