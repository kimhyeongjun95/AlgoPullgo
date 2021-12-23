import heapq


def solution(n, works):
    if n >= sum(works):
        return 0

    answer = 0
    works = [-i for i in works]
    heapq.heapify(works)
    while n:
        n -= 1
        temp = heapq.heappop(works) + 1
        heapq.heappush(works, temp)

    for work in works:
        answer += work ** 2

    return answer
