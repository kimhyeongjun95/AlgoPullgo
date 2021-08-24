import sys
input = sys.stdin.readline

# 1

def find_NGE(arr, N):
    result = [-1] * N
    
    for i in range(N): # 3 5 2 7
        stack = []
        j = 1
        while i + j < N:
            if len(stack) == 0 and arr[i] < arr[i+j]:
                stack.append(arr[i+j])
                result[i] = stack[-1]
            j += 1
    return result

N = int(input())                         
arr = list(map(int, input().split()))  
print(*find_NGE(arr, N))
    

# 2

# N = int(input())                         
# arr = list(map(int, input().split()))  
# stack = []
# result = [-1] * N     
# for i in range(N):    
#     j = 1
#     while i + j < N:
#         if arr[i] < arr[i+j]:
#             result[i] = arr[i+j]
#             break    
#         j += 1
# print(*result)
  

