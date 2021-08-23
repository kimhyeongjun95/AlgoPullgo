def dfs(arr, v):
    global count
    stack = []
    stack.append(v)

    while stack:
        v = stack.pop()

        if visited[v] == 0:
            visited[v] = 1
            count += 1

            for i in arr[v]:
                if visited[i] == 0:
                    stack.append(i)
                    
    return count


n = int(input())
pair = int(input())

arr = [[] * (n+1) for _ in range(n+1)]

for _ in range(pair):
    one, two = map(int, input().split())
    arr[one].append(two)
    arr[two].append(one)

# print(arr)

visited = [0] * (n+1)
count = -1 # 처음에 1은 count한걸로 안봐야함, 영항을 준 것이 아니기 때문에
result = dfs(arr, 1)
print(result) 