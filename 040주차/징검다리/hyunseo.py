# 프로그래머스 징검다리

def solution(distance, rocks, n):
    rocks.sort(reverse = True)
    
    dist = []
    
    this = 0
    while rocks:
        dist.append(rocks[-1] - this)
        this = rocks.pop()
    
    dist.append(distance - this)
    
    for _ in range(n):
        min_idx = dist.index(min(dist))
        
        if min_idx == 0:
            min_val = dist.pop(0)
            dist[0] += min_val
        elif min_idx == len(dist)-1:
            min_val = dist.pop()
            dist[-1] += min_val
        else:
            if dist[min_idx-1] < dist[min_idx+1]:
                min_val = dist.pop(min_idx)
                dist[min_idx-1] += min_val
            else:
                min_val = dist.pop(min_idx)
                dist[min_idx] += min_val
    
    return min(dist)


print(solution(25, [2, 14, 11, 21, 17], 2))

# 반례
# 16, [4, 8, 11], 2
# 답: 8
# 글쓴이 오답 : 5