# 5052번 전화번호 목록
import sys
input = sys.stdin.readline


class Node:
    def __init__(self, key, data=None):
        self.data = data
        self.key = key
        self.next = dict()


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, string):
        curr = self.root
        for char in string:
            if not char in curr.next:
                curr.next[char] = Node(char)
            curr = curr.next[char]
        curr.data = string

    def search(self, string):
        curr = self.root
        for char in string:
            if char in curr.next:
                curr = curr.next[char]
            else:
                return False
        if curr.data:
            return True

    def startwith(self, string):
        curr = self.root

        for p in string:
            if p in curr.next:
                curr = curr.next[p]
            else:
                return False

        return True


def solution(strings):
    trie = Trie()
    for string in strings:
        if trie.startwith(string):
            return False
        else:
            trie.insert(string)
    return True


for _ in range(int(input())):
    N = int(input())
    strings = [input().strip() for _ in range(N)]
    strings.sort(key=lambda x: -len(x))

    print('YES') if solution(strings) else print('NO')
