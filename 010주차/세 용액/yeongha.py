# 세 용액
def two_pointer(lst, start, end):
    global mark, answer_sum, flag
    left, right = start, end

    while left < right:
        total = mark + lst[left] + lst[right]

        if abs(total) < answer_sum:
            answer[0] = mark
            answer[1] = lst[left]
            answer[2] = lst[right]
            answer_sum = abs(total)
                
            if total == 0:
                flag = True
                break
        
        if total > 0:
            right -= 1
        elif total < 0:
            left += 1
    
    
N = int(input())
nums = list(map(int,input().split()))
nums.sort()
answer_sum = float('inf')
answer = [0]*3
flag = False
for i in range(N-2):
    mark = nums[i]
    two_pointer(nums, i+1, N-1)
    if flag:
        break
print(*answer)

