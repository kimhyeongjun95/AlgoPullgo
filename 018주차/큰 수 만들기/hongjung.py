def solution(number, k):
    number = list(map(str, number))

    stack = []
    flag = False
    for i in range(len(number)):
        if stack:
            while stack:
                if int(stack[-1]) < int(number[i]):
                    stack.pop()
                    k -= 1
                    if k == 0:
                        flag = True
                        break
                else:
                    break
            stack.append(number[i])
            if flag:
                answer = ''
                for n in stack:
                    answer += n
                for n in number[i+1:]:
                    answer += n
                return answer
        else:
            stack.append(number[i])

    if k:
        while k:
            stack.pop()
            k -= 1

    answer = ''
    for n in stack:
        answer += n
    return answer

    
# from itertools import combinations

# def solution(number, k):
#     number = list(map(str, number))
#     length = len(number) - k

#     numbers = combinations(number, length)

#     answer = '0'
#     for nums in numbers:
#         tmp = ''
#         for n in nums:
#             tmp += n
#         if int(tmp) > int(answer):
#             answer = tmp
#     return answer


# def solution(number, k):
    
#     def make_num(nums, k, cnt):
#         nonlocal answer
#         if int(answer[0]) > int(nums[0]):
#             return
            
#         if k == cnt:
#             result = ''
#             for n in nums:
#                 result += str(n)
#             if int(result) > int(answer):
#                 answer = result
#             return

#         for i in range(len(nums)):
#             a = nums.pop(i)
#             make_num(nums, k, cnt+1)
#             nums.insert(i, a)

#     answer = '0'
#     number = list(map(str, number))
#     make_num(number, k, 0)
#     return answer


# def solution(number, k):
#     number = list(map(int, number))

#     max_idx = 0
#     max_num = 0
#     for i in range(len(number)):
#         if number[i] > max_num:
#             max_idx = i
#             max_num = number[i]

#     while k > 0:
#         if number[:max_idx]:
#             number.remove(min(number[:max_idx]))
#             max_idx -= 1
#             k -= 1
#         else:
#             number.remove(min(number))
#             k -= 1
    
#     answer = ''
#     for n in number:
#         answer += str(n)
#     return answer
