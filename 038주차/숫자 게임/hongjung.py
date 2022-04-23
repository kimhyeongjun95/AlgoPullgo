# def solution(A, B):
#     B.sort()
#     length = len(A)
#     check = [0] * length
#     idx = 0
#     while idx < length:
#         for i in range(length):
#             if check[i] == 0 and B[idx] > A[i]:
#                 check[i] = 1
#                 break
#         idx += 1

#     answer = sum(check)
#     return answer


def solution(A, B):
    A.sort()
    B.sort()
    length = len(A)
    a_idx, b_idx = 0, 0
    answer = 0
    while a_idx != length and b_idx != length:
        if B[b_idx] > A[a_idx]:
            answer += 1
            a_idx += 1
            b_idx += 1
        else:
            b_idx += 1
    return answer

print(solution([5,1,3,7], [2,2,6,8]))
print(solution([2,2,2,2], [1,1,1,1]))