def dfs(tickets, l):
    visited = [0]*l
    stack = [(["ICN"], 0, visited)]
    cand = []

    while stack:
        rout, cnt, visited = stack.pop()

        if cnt == l:
            cand.append(rout)
            continue
            
        for i in range(l):
            if not visited[i] and tickets[i][0] == rout[-1]:
                visited[i] = 1
                temp = visited[:]
                stack.append((rout+[tickets[i][1]], cnt+1, temp))
                visited[i] = 0
    
    return cand

def solution(tickets):
    l = len(tickets)
    cand = dfs(tickets, l)
    asnwer = sorted(cand)[0]
    return asnwer
    

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))