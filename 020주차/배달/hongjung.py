from collections import defaultdict, deque

def solution(N, road, K):
    def bfs():
        nonlocal distance_list, adj_list

        queue = deque([])
        distance_list[1] = 0
        for adj in adj_list[1]:
            queue.append(adj)
        for q in queue:
            if q[1] < distance_list[q[0]]:
                distance_list[q[0]] = q[1]
       
        while queue:
            point, distance = queue.popleft()
            for adj in adj_list[point]:
                if distance + adj[1] < distance_list[adj[0]]:
                    distance_list[adj[0]] = distance + adj[1]
                    queue.append([adj[0], distance + adj[1]])
    
    adj_list = defaultdict(list)
    for a, b, c in road:
        adj_list[a].append([b, c])
        adj_list[b].append([a, c])

    distance_list = [float('inf')] * (N + 1)
    bfs()

    answer = 0
    for d in distance_list[1:]:
        if d <= K:
            answer += 1
    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))