# 프로그래머스 입국 심사

def solution(n, times):
    
    # n: 입국 심사를 기다리는 사람 수
    # times : 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열
    # return 모든 사람이 심사를 받는데 걸리는 시간의 최솟값

    answer = 0
    left = 1
    right = max(times) * n

    while left < right:
        mid = (left + right) // 2
        temp = 0

        for time in times:
            temp += mid // time

        # 심사한 사람수가 n 이상
        if temp >= n:
            answer = mid
            right = mid - 1
        
        # 심사한 사람수가 n 미만
        elif temp < n:
            left = mid + 1

    return answer

print(solution(6, [7, 10])) # 28