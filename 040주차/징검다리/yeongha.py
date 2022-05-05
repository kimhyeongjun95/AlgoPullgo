def solution(distance, rocks, n):
    start, end = 0, distance
    
    rocks.sort()
    
    while start < end: 
        mid = (start + end) // 2
        cnt = 0
        pre_stone = 0 
        for rock in rocks:
            if rock - pre_stone <  mid:
                cnt += 1 
            else:
                pre_stone = rock
        
            if cnt > n:
                break
                
        if cnt > n:
            end = mid
        else:
            start = mid + 1
            
    return start - 1