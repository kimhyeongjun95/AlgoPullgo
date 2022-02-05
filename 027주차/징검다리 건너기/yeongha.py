def solution(stones, k):
    answer = 0
    start, end = 1, max(stones)
    while start <= end:
        middle = (start + end)//2

        max_cnt = 0
        cnt = 0
        flag = False
        for stone in stones:
            if stone - middle <= 0:
                if flag:
                    cnt += 1
                else:
                    max_cnt = max(max_cnt, cnt)
                    cnt = 1
                    flag = True
            else:
                flag = False
                         
        max_cnt = max(max_cnt, cnt)

        if max_cnt >= k:
            answer = middle
            end = middle - 1
        else:
            start = middle + 1
    
    return answer