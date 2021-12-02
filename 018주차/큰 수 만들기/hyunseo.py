# 프로그래머스 큰 수 만들기
# from collections import deque

# def find_max(number, need):
#     idx = -1
#     num = 0

#     for i in range(len(number)-need+1):
#         if int(number[i]) > num:
#             idx = i
#             num = int(number[i])
    
#     return num, idx


# def solution(number, k):
#     # 필요한 자릿수 = len(number) - k
#     # -> 이만큼의 숫자를 뽑는다!

#     need = len(number) - k
#     number = deque(number)
#     answer = ''

#     while number and need:
#         if len(number) == need:
#             while number:
#                 answer += str(number.popleft())
#             break

#         num, idx = find_max(number, need)

#         answer += str(num)
#         for _ in range(idx+1):
#             number.popleft()
#         need -= 1

#     return answer


def solution(number, k):
    stack = []

    for num in number:
        while k and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    answer = ''.join(stack[:len(number)-k])
    return answer

print(solution('1924', 2))
print(solution('1231234', 3))
print(solution('4177252841', 4))
print(solution('99991', 3))