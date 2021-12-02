# from itertools import combinations

# def solution(number, k):
#     perms = list(combinations(number, len(number) - k))
#     numbers = []
#     for perm in perms:
#         numbers.append(''.join(perm))
#     return max(numbers)


def solution(number, k): 
    num = list(number)
    stack = [num[0]] 
    count = 0 
    
    for i in range(1, len(num)): 
        if count == k: 
            stack = stack + num[i:] 
            break 
         
        stack.append(num[i]) 
        if stack[-1] > stack[-2]: 
            while(len(stack) != 1 and stack[-1] > stack[-2] and count < k): 
                stack[-2], stack[-1] = stack[-1], stack[-2] 
                stack.pop() 
                count += 1 
    
    return "".join(stack[:len(num)-k])

