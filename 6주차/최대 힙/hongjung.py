import sys
import heapq

N = int(sys.stdin.readline())
cmd = [int(sys.stdin.readline()) for _ in range(N)]

numbers = []
for c in cmd:
    if c:
        heapq.heappush(numbers, [-c, c]) # 나중에 최대값을 pop해주기 위해 음수와 양수 형태의 c 리스트를 푸쉬해줌
    else:
        if numbers: # 숫자가 있다면
            print(heapq.heappop(numbers)[1]) # 소리스트의 첫번째 원소를 기준으로 가장 작은 리스트가 pop이 됨, 이때 인덱싱을 통해 뒤의 양수를 출력
        else:
            print(0)