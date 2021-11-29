import sys

def find_max(nums, idx, n, ops, num):
    global result
    if idx == n:
        if num < result[1]:
            result[1] = num
        if num > result[0]:
            result[0] = num
        return
    
    for i in range(4):
        if ops[i]:
            if i == 0:
                new_num = num + nums[idx]
                ops[0] -= 1
                find_max(nums, idx+1, n, ops, new_num)
                ops[0] += 1
            if i == 1:
                new_num = num - nums[idx]
                ops[1] -= 1
                find_max(nums, idx+1, n, ops, new_num)
                ops[1] += 1
            if i == 2:
                new_num = num * nums[idx]
                ops[2] -= 1
                find_max(nums, idx+1, n, ops, new_num)
                ops[2] += 1
            if i == 3:
                if num < 0:
                    new_num = abs(num) // nums[idx]
                    ops[3] -= 1
                    find_max(nums, idx+1, n, ops, -new_num)
                    ops[3] += 1
                else:
                    new_num = num // nums[idx]
                    ops[3] -= 1
                    find_max(nums, idx+1, n, ops, new_num)
                    ops[3] += 1


N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
operations = list(map(int,sys.stdin.readline().split()))

result = [float('-inf'), float('inf')]

find_max(numbers, 1, N, operations, numbers[0])

for i in result:
    print(i)