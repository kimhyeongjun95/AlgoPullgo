# 프로그래머스 입국심사

def solution(n, times):
    answer = 0

    left = 1
    right = n * max(times)

    while left <= right:
        mid = (left + right) // 2

        count = 0
        for time in times:
            count += mid // time
            if count >= n:
                break

        if count >= n:
            answer = mid
            right = mid - 1
        # 없는 경우
        elif count < n:
            left = mid + 1

    return answer
