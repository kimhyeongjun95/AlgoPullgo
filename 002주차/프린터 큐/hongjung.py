import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))

    target = str(numbers[M]) # 찾고자 하는 인덱스의 숫자를 문자형으로 따로 저장([1, 1, 9, 1, 1, 1] 같은 경우 찾고자 하는 숫자를 구별할 수 없으므로!)

    deque1 = deque(numbers[:])
    deque1[M] = target # deque의 찾고자 하는 인덱스의 숫자도 문자형으로 바꿔줌
    cnt = 0
    while True:
        if int(deque1[0]) == max(list(map(int, deque1))): # 찾고자 하는 인덱스의 숫자는 문자형이므로 항상 정수형으로 변환, deque 안에 문자형이 있으므로 다시 정수형 리스트로 변환 후 비교
            if deque1[0] == target:
                cnt += 1
                break
            else:
                deque1.popleft()
                cnt += 1
        else:
            deque1.append(deque1[0])
            deque1.popleft()
    print(cnt)