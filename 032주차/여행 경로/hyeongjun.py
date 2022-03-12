# 프로그래머스 여행경로

# 경로가 2개 이상이면 알파벳 순서

from collections import defaultdict
def solution(tickets):

    way = defaultdict(list)
    for ticket in tickets:
        way[ticket[0]].append(ticket[1])
    
    for i in way:
        way[i].sort(reverse = True)

    answer = []
    stack = ["ICN"]
    
    while stack:
        if stack[-1] not in way or len(way[stack[-1]]) == 0:
            answer.append(stack.pop())
        else:
            popped = way[stack[-1]].pop()
            stack.append(popped)
    answer = answer[::-1]
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	))
# ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	))
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
