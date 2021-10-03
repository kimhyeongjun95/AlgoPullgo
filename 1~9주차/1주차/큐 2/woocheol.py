# 18258번 큐2
import sys
from collections import deque
input = sys.stdin.readline


class QUEUE:
    def __init__(self):
        self.queue = deque()
        self.length = 0

    # push X: 정수 X를 큐에 넣는 연산이다.
    def push(self, num):
        self.queue.append(num)
        self.length += 1

    # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def popQ(self):
        if self.queue:
            self.length -= 1
            return self.queue.popleft()
        return -1
    # size: 큐에 들어있는 정수의 개수를 출력한다.

    def size(self):
        return self.length

    # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    def empty(self):
        return 0 if self.length else 1

    # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def front(self):
        return self.queue[0] if self.queue else -1

    # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def back(self):
        return self.queue[self.length-1] if self.queue else -1


N = int(input())
queue = QUEUE()
for _ in range(N):
    command = list(input().strip().split())

    if command[0] == 'push':
        queue.push(command[1])
    elif command[0] == 'pop':
        print(queue.popQ())
    elif command[0] == 'size':
        print(queue.size())
    elif command[0] == 'empty':
        print(queue.empty())
    elif command[0] == 'front':
        print(queue.front())
    elif command[0] == 'back':
        print(queue.back())
