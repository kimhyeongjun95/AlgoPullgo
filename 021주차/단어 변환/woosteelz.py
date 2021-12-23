import sys
from collections import deque


def solution(begin, target, words):
    if not target in words:
        return 0
    words.append(begin)
    graph = dict()
    for i in range(len(words)):
        temp = []
        for j in range(len(words)):
            if differ_word(words[i], words[j]):
                temp.append(words[j])
        graph[words[i]] = temp

    visited = dict()
    for a in words:
        visited[a] = False
    stack = deque()
    stack.append(begin)
    visited[begin] = True
    cnt = 0
    while stack:
        word = stack[-1]
        if word == target:
            return cnt
        for a in graph[word]:
            if not visited[a]:
                visited[a] = True
                stack.append(a)
                cnt += 1
                break
        else:
            stack.pop()
            cnt -= 1


def differ_word(a, b):
    a = list(a)
    b = list(b)
    for i in a:
        if i in b:
            b.remove(i)
    if len(b) == 1:
        return True
    return False
