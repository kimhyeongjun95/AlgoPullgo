import sys

T = int(sys.stdin.readline())

for _ in range(T):
    W = sys.stdin.readline().rstrip()
    K = int(sys.stdin.readline())

    W_dict = {key : [] for key in W} # W 안의 문자열이 KEY인 빈 딕셔너리 생성 

    for i in range(len(W)):
        W_dict[W[i]].append(i) # 딕셔너리에 각 문자열의 인덱스 리스트를 만들어 줌
    
    result = []
    for k, v in W_dict.items():
        if len(v) >= K: # 만약 문자열의 인덱스가 K개 이상이면
            for i in range(len(v)-K+1): # K-1 간격 만큼 인덱스를 빼주고 그 차이를 result에 저장
                result.append(v[i+K-1] - v[i] + 1)
    
    if result == []: # result가 빈 리스트이면 -1 출력
        print(-1)
    else: # 그게 아니면 result의 최댓값, 최솟값 차례로 출력
        print(min(result), end=' ')
        print(max(result))






    # i = 0
    # j = 0
    # cnt = 0
    # result = []
    # while i < len(W) - 1:
    #     if j == len(W):
    #         i += 1
    #         j = i
    #         cnt = 0
    #     if W[i] == W[j]:
    #         cnt += 1
    #         if cnt == K:
    #             result.append(j - i + 1)
    #             i += 1
    #             j = i
    #             cnt = 0
    #         else:
    #             j += 1
    #     else:
    #         j += 1
    
    # if result == []:
    #     print(-1)
    # else:
    #     result.sort()
    #     print(result[0], end=' ')
    #     print(result[-1])




    # length = []
    # i = 0
    # while i < len(W):
    #     minus = K
    #     plus = 1
    #     for j in range(i, len(W)):
    #         if W[i] == W[j]:
    #             minus -= 1
    #             if minus == 0:
    #                 length.append(plus)
    #                 break
    #             plus += 1
    #         else:
    #             plus += 1
    #     i += 1
    
    # result = ''
    # if len(length) == 0:
    #     result = '-1'
    # else:
    #     result += (str(min(length)) + ' ' + str(max(length)))

    # print(result)