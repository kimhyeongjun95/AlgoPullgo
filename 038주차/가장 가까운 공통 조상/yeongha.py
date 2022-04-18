import sys
sys.setrecursionlimit(10**5)

def find(a, b, a_parents, b_parents):
    global answer
    new_a = nodes[a]
    new_b = nodes[b]

    if new_a == new_b:
        answer = new_a
        return
    elif a_parents[new_b]:
        answer = new_b
        return
    elif b_parents[new_a]:
        answer = new_a
        return
    else:
        a_parents[new_a] = 1
        b_parents[new_b] = 1
        find(new_a, new_b, a_parents, b_parents)


input = sys.stdin.readline
tc = int(input().rstrip())
for _ in range(tc):
    answer = -1
    N = int(input().rstrip())
    nodes = [0 for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().rstrip().split())
        nodes[b] = a
    n, m = map(int, input().rstrip().split())
    a_parents = [0 for _ in range(N+1)]
    b_parents = [0 for _ in range(N+1)]
    a_parents[n] = 1
    b_parents[m] = 1
    find(n, m, a_parents, b_parents)
    print(answer)