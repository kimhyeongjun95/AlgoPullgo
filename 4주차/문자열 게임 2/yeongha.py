# 문자열 게임2
from collections import defaultdict

# 완전 탐색 효율성 최악
# def string_game1(W, K):
#     for i in range(K, len(W)):
#         for j in range(0, len(W)-i):
#             string = list(W[j:j+i])
#             for k in set(string):
#                 if string.count(k) == K:
#                     print(i, string_game2(j, j+i-1, W))
#                     return
#     print(-1)
#     return

def string_game(W, K):
    if K == 1:  # K가 1일때는 문자열의 길이가 무조건 1
        return [1, 1]
    alphabet = defaultdict(int)

    for i in W:
        alphabet[i] += 1  # 각 알파벳들의 수를 딕셔너리에 저장
    min_interval = len(W)-1
    max_interval = 0
    for key, value in alphabet.items():
        if value >= K:  # 여러 알파벳 중 K개 이상인 알파벳만 확인
            index_list = list(filter(lambda x: W[x] == key, range(len(W))))  # 해당 알파벳의 인덱스 구하기

            for j in range(len(index_list)-K+1):
                start, end = index_list[j], index_list[j+K-1]
                if end - start < min_interval:
                    min_interval = end - start
                if end - start > max_interval:
                    max_interval = end - start

    if max_interval == 0:  # 문자열 못 찾음
        return [-1]
    return [min_interval+1, max_interval+1]

# 혼자 문제 지어내서 푼 코드ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
# 4. 3번에서 구한 문자를 포함하고 첫번째와 마지막 글자가 같은 가장 짧은 문자열을 구하는 코드;;
# def string_game2(s, e, string):
#     left = []
#     right = []
#     temp = 1
#     while e+temp < len(string) and s-temp > 0:
#         left += string[s-temp]
#         right += string[e+temp]
#         for i in range(len(left)):
#             for j in range(len(right)):
#                 if left[i] == right[j]:
#                     l, r= i+1, j+1
#                     return l + (e-s+1) + r
#         temp += 1
#     return -1

T = int(input())
for _ in range(T):
    W = input()
    K = int(input())
    print(*string_game(W, K))
