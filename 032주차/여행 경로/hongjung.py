def solution(tickets):
    def bfs(airport, track):
        nonlocal route, visited, answer

        if len(answer) < len(track):
            answer = track
        
        for i in range(len(tickets)):
            if tickets[i][0] == airport and visited[i] == False:
                visited[i] = True
                bfs(tickets[i][1], track + [tickets[i][1]])
                visited[i] = False

    answer = []
    visited = [False] * len(tickets)
    tickets.sort(key=lambda x: (x[0], x[1]))
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            route = []
            visited[i] = True
            route.append(tickets[i][0])
            route.append(tickets[i][1])
            bfs(tickets[i][1], route)
            visited[i] = False
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))