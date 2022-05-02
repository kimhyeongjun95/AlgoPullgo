def solution(n, results):
    answer = 0
    winner = [[] for _ in range(n+1)]
    loser = [[] for _ in range(n+1)]
    
    for w,l in results:
        winner[w].append(l)
        loser[l].append(w)
    print(winner)
    print(loser)
    
    for i in range(1,n+1):
        for w in winner[i]:
            for l in loser[i]:
                if l not in loser[w]:
                    loser[w].append(l)
                if w not in winner[l]:
                    winner[l].append(w)
    print(winner)
    print(loser)
    for i in range(n+1):
        if len(winner[i]) + len(loser[i]) == n-1:
            answer += 1
    
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))