import heapq

def solution(operations):
    data = []
    for o in operations:
        tmp = o.split()
        if tmp[0] == 'I':
            heapq.heappush(data, int(tmp[1]))
        else:
            if data:
                if tmp[1] == '-1':
                    heapq.heappop(data)
                else:
                    tmp_data = []
                    while len(data) > 1:
                        heapq.heappush(tmp_data, heapq.heappop(data))
                    data = tmp_data
    if data:
        answer = [max(data), min(data)]
    else:
        answer = [0, 0]
    return answer

print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))
print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))