def solution(n, wires):
    answer = float('inf')
    graph = [[] for _ in range(n+1)]

    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])

    for wire in wires:
        A, B = [wire[0]], [wire[1]]
        visited = [False] * (n+1)
        visited[A[0]] = True
        visited[B[0]] = True
        cnt_A, cnt_B = 0, 0
        
        while A:
            pop_A = A.pop(0)
            for i in graph[pop_A]:
                if not visited[i]:
                    A.append(i)
                    cnt_A += 1
                    visited[i] = True

        while B:
            pop_B = B.pop(0)
            for i in graph[pop_B]:
                if not visited[i]:
                    B.append(i)
                    cnt_B +=1
                    visited[i] = True

        answer = min(answer, abs(cnt_A - cnt_B))

    return answer