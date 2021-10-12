import sys
from itertools import combinations

def dfs(n, list1):
    visited = [False for _ in range(N+1)]
    stack = [n]
    result = [n]
    while stack:
        x = stack.pop()
        for i in area[x]:
            if visited[i] == False and i in list1:
                stack.append(i)
                visited[i] = True
                result.append(i)
    
    if list(set(result)) == list1:
        return True
    else:
        return False


N = int(sys.stdin.readline())
area_num = [0] + list(map(int, sys.stdin.readline().split()))

population = {}
for i in range(1, N+1):
    population[i] = area_num[i]

area = [[] for _ in range(N+1)]
for i in range(1, N+1):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in temp[1:]:
        area[i].append(j)

powerset = []
for i in range(1, N):
    for j in combinations(range(1, N+1), i):
        powerset.append(j)

result = float('inf')

for i in powerset:
    i_flag = False
    if len(i) == 1:
        i_flag = True
    else:
        for j in i:
            if dfs(j, i) == False:
                break
        else:
            i_flag = True
    if i_flag:
        i_minus = []
        for k in range(1, N+1):
            if k not in i:
                i_minus.append(k)

        i_minus_flag = False
        for j in i_minus:
            if dfs(j, i_minus) == False:
                break
            else:
                i_minus_flag = True
        
        if i_minus_flag:
            temp1 = 0
            for j in i:
                temp1 += population[j]
            temp2 = 0
            for j in i_minus:
                temp2 += population[j]
            
            if result > abs(temp1 - temp2):
                result = abs(temp1 - temp2)
    
if result == float('inf'):
    print(-1)
else:
    print(result)