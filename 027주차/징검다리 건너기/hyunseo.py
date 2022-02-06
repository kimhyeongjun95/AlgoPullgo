# 프로그래머스 징검다리 건너기

def solution(stones, k):  
    min_people = min(stones)
    max_people = max(stones)
    
    answer = 0
    while min_people <= max_people:
        mid = (min_people + max_people) // 2
        array = [stone - mid for stone in stones] # mid명의 친구가 징검다리를 건넌 뒤 디딤돌에 적힌 숫자
        
        cnt = 0
        for a in array:
            if a <= 0:
                cnt += 1
                if cnt >= k:
                    break
            else:
                cnt = 0
        
        if cnt >= k:
            max_people = mid - 1
            answer = mid
        else:
            min_people = mid + 1
    
    return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
print(solution(stones, 1))