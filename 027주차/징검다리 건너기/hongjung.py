def solution(stones, k):
    length = len(stones)
    left = 1
    right = 200000000
    while left <= right:
        mid = (left + right) // 2
        stones_copy = stones[:]
        for i in range(length):
            if stones_copy[i] - mid <= 0:
                stones_copy[i] = 0
            else:
                stones_copy[i] -= mid
        
        check = 0
        check_list = []
        for i in range(length):
            if stones_copy[i] == 0:
                check += 1
            else:
                if check not in check_list:
                    check_list.append(check)
                check = 0
        if check not in check_list:
            check_list.append(check)

        if max(check_list) >= k:
            right = mid - 1
        else:
            left = mid + 1
    return left

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))