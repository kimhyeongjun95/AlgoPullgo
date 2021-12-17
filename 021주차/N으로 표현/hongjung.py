# 테케 4개 시간초과 수정중...
def solution(N, number):
    def make_min_cnt(current):
        nonlocal nums, number, answer, tmp_nums, tmp_cnts
        cnt = 0
        for i in range(len(tmp_nums)):
            if tmp_nums[i] == current:
                cnt = tmp_cnts[i]
                break
        
        if cnt > 8:
            return

        if current == number:
            if answer > cnt:
                answer = cnt
            return

        current_idx = tmp_nums.index(current)
        for i in range(1, len(nums)):
            if current + int(nums[i]) not in tmp_nums:
                tmp_nums.append(current + int(nums[i]))
                tmp_cnts.append(tmp_cnts[current_idx] + i)
                make_min_cnt(current + int(nums[i]))
                tmp_nums.pop()
                tmp_cnts.pop()
            else:
                after_idx = tmp_nums.index(current + int(nums[i]))
                origin = tmp_cnts[after_idx]
                if origin > tmp_cnts[current_idx] + i:
                    tmp_cnts[after_idx] = tmp_cnts[current_idx] + i
                    make_min_cnt(current + int(nums[i]))
                    tmp_cnts[after_idx] = origin

            if current - int(nums[i]) not in tmp_nums:
                tmp_nums.append(current - int(nums[i]))
                tmp_cnts.append(tmp_cnts[current_idx] + i)
                make_min_cnt(current - int(nums[i]))
                tmp_nums.pop()
                tmp_cnts.pop()
            else:
                after_idx = tmp_nums.index(current - int(nums[i]))
                origin = tmp_cnts[after_idx]
                if origin > tmp_cnts[current_idx] + i:
                    tmp_cnts[after_idx] = tmp_cnts[current_idx] + i
                    make_min_cnt(current - int(nums[i]))
                    tmp_cnts[after_idx] = origin

            if current * int(nums[i]) not in tmp_nums:
                tmp_nums.append(current * int(nums[i]))
                tmp_cnts.append(tmp_cnts[current_idx] + i)
                make_min_cnt(current * int(nums[i]))
                tmp_nums.pop()
                tmp_cnts.pop()
            else:
                after_idx = tmp_nums.index(current * int(nums[i]))
                origin = tmp_cnts[after_idx]
                if origin > tmp_cnts[current_idx] + i:
                    tmp_cnts[after_idx] = tmp_cnts[current_idx] + i
                    make_min_cnt(current * int(nums[i]))
                    tmp_cnts[after_idx] = origin

            if current // int(nums[i]) not in tmp_nums:
                tmp_nums.append(current // int(nums[i]))
                tmp_cnts.append(tmp_cnts[current_idx] + i)
                make_min_cnt(current // int(nums[i]))
                tmp_nums.pop()
                tmp_cnts.pop()
            else:
                after_idx = tmp_nums.index(current // int(nums[i]))
                origin = tmp_cnts[after_idx]
                if origin > tmp_cnts[current_idx] + i:
                    tmp_cnts[after_idx] = tmp_cnts[current_idx] + i
                    make_min_cnt(current // int(nums[i]))
                    tmp_cnts = origin

    limit_num = number // 10
    nums = [0]
    answer = float('inf')
    for i in range(limit_num+1):
        nums.append(str(N) + str(N) * i)
    for i in range(1, len(nums)):
        tmp_nums = []
        tmp_cnts = []
        tmp_nums.append(int(nums[i]))
        tmp_cnts.append(i)
        make_min_cnt(int(nums[i]))

    if answer == float('inf'):
        return -1
    return answer

print(solution(5, 12))
print(solution(2, 11))
