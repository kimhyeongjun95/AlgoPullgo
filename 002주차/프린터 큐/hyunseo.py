import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    document = deque(map(int, sys.stdin.readline().split()))

    i = 0

    # 만약 타겟 문서가 인쇄되었다면 M = -1
    while M >= 0:

        if document[0] == max(document):
            document.popleft()
            i += 1  # 인쇄 횟수 +1
            N -= 1  # 남은 문서 개수 -1
            M -= 1  # 타겟 문서 한 칸 앞으로
        else:
            document.append(document.popleft())

            # M이 0일 경우 N-1을 더해서 맨 뒤로 이동
            if not M:
                M += (N-1)
            # M이 0이 아닐 경우 1을 빼서 한 칸씩 앞으로 이동
            else:
                M -= 1

    print(i)