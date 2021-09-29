# 백준 14501 퇴사

N = int(input())

term = [0]
pay = [0]
for _ in range(N):
    T, P = map(int, input().split())
    term.append(T)
    pay.append(P)

arr = [[0 for _ in range(N+1)] for _ in range(N+1)]

# i : i일에 일을 시작
for i in range(1, N+1):
    # i일에 일을 시작한다면 끝나는 날
    finish = i - 1 + term[i]

    # j : 현재 날짜
    for j in range(1, N+1):
        if j < finish:
            # 일을 끝낼 수 없음
            # -> 일을 수행하지 않을 때의 금액 그대로 가져오기
            arr[i][j] = arr[i-1][j]

        else:
            # 일을 끝낼 수 있음
            # -> 일을 수행할 때와 안 할때의 금액을 비교

            # 일을 시작한 날 이전까지의 최대 금액 + 금액
            do = arr[i-1][i-1] + pay[i]
            dont = arr[i-1][j]

            arr[i][j] = max(do, dont)

# for row in arr:
#     print(row)

print(arr[N][N])