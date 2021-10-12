from itertools import combinations

def dfs(n):
    total = 0
    stack = [n]
    visited.remove(n)

    while stack:
        v = stack.pop()
        total += population[v]

        for j in node[v]:
            if j in visited:
                visited.remove(j)
                stack.append(j)
    return total

N = int(input())
population = [0] + list(map(int, input().split()))
population_sum = sum(population)
node  = {}
ans = 9999

for i in range(1, N+1):
    lst = list(map(int, input().split()))
    node[i] = lst[1:]

area = [i for i in range(1, N+1)]
for i in range(1, N):
    for item in combinations(area, i):
        visited = list(item)
        t = dfs(visited[0])

        if not visited:
            diff = abs((population_sum - t)-t)

            if diff < ans:
                visited = list(set(area) - set(item))
                dfs(visited[0])

                if not visited:
                    ans = diff

if ans == 9999:
    print(-1)
else:
    print(ans)



