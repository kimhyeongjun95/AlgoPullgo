import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
num_deque = deque(range(1, N+1)) # 연산 속도와 popleft, appendleft를 사용하기 위해 deque를 사용

cnt = 0 # 2번, 3번 연산을 카운트 하기 위한 변수
for i in numbers:
    while True:
        if i == num_deque[0]: # 만약 뽑아내려고 하는 수가 이미 deque의 첫 번째 인덱스라면 pop하고 break
            num_deque.popleft()
            break
        else: # 그게 아니라면
            if num_deque.index(i) >= len(num_deque) / 2: # 먼저 그 수가 deque 길이의 절반 이상에 위치하고 있는지 확인
                num_deque.appendleft(num_deque[-1]) 
                num_deque.pop()
                cnt += 1 # 절반 이상에 위치하고 있다면 맨 끝에 수를 맨 앞에 추가해주고 삭제
            else:
                num_deque.append(num_deque[0])
                num_deque.popleft()
                cnt += 1 # 절반 이하에 위치하고 있다면 맨 앞에 수를 맨 뒤에 추가해주고 삭제

print(cnt)