# 프로그래머스 징검다리 건너기

# def solution(stones, k):
#     # 0이 아닌 최솟값을 찾아서 0으로 만들면서 0과의 차이만큼 answer += 하기
#     answer = 0

#     while True:
#         min_number = max(stones)
#         # 최솟값 찾기
#         for i in stones:
#             if i < min_number and i > 0:
#                 min_number = i

#         count = 0
#         for i in range(len(stones)):
#             if stones[i] == 0:
#                 count += 1
#                 if count >= k:
#                     return answer
#             else:
#                 count = 0
#                 stones[i] -= min_number
#         answer += min_number

def solution(stones, k):
    left = 1
    right = max(stones)
    
    while left <= right:
        mid = (left+right) // 2
        count = 0
        for stone in stones:
            if stone - mid <= 0:
                count += 1
                if count == k:
                    break
            else:
                count = 0
        
        if count == k:
            right = mid - 1
        else:
            left = mid + 1
            answer = left
    
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)) # 3
print(solution([3, 4, 8, 2, 1, 1, 3, 2], 4)) # 3