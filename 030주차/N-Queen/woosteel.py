def get_list(n, visited, curr, res):
    for x in range(len(curr)):
        for y in range(x+1, len(curr)):
            if abs(curr[x] - curr[y]) == abs(x - y):
                return

    if len(curr) == n:
        res.append(curr)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            curr.append(i)
            get_list(n, visited, curr, res)
            visited[i] = False
            curr.pop()


def solution(n):
    res = []
    get_list(n, [False for _ in range(n)], [], res)
    return len(res)
