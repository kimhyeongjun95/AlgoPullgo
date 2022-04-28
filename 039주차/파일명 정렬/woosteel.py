# 프로그래머스 파일명 정렬(Level 2)
from collections import deque

def solution(files):
	answer = []
	new_files = []
	
	for f in files:
		k = f.lower()
		k = deque(k)
		head = ''
		number = ''
		tail = ''
		while k:
			i = k.popleft()
			if i.isdigit():
				k.insert(0, i)
				break
			else:
				head += i
		while k:
			i = k.popleft()
			if i.isdigit():
				number += i
			else:
				k.insert(0, i)
				break
		while k:
			tail += k.popleft()	
		answer.append([head, int(number), tail, f])
		answer.sort(key=lambda x:(x[0], x[1]))
		ans = []
		for a in answer:
			ans.append(a[3])

	return ans