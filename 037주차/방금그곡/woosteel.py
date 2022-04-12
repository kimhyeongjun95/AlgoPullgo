# 프로그래머스 방금그곡(Level 2)
from collections import deque

def solution(m, musicinfos):
	answer = []
	new_music = []
	new_m = []
	m = list(m)
	for i in m:
		if i == '#':
			new_m[-1] = new_m[-1].lower()
		else:
			new_m.append(i)
	new_m = ''.join(new_m)
	for i in range(len(musicinfos)):
		new_info = list(musicinfos[i].split(','))
		h1, m1 = new_info.pop(0).split(':')
		h2, m2 = new_info.pop(0).split(':')
		minutes = (int(h2)-int(h1))*60 + int(m2)-int(m1)
		name = new_info[0]
		muse = list(new_info[1])
		new_muse = []
		for j in muse:
			if j == '#':
				new_muse[-1] = new_muse[-1].lower()
			else:
				new_muse.append(j)
		new_music.append([name, ''.join(new_muse), minutes])

	for music in new_music:
		a = music[2] // len(music[1])
		b = music[2] % len(music[1])
		temp = music[1] * a + music[1][:b]
		if new_m in temp:
			answer.append([music[0], music[2]])
	answer.sort(key = lambda x:x[1], reverse = True)

	if answer:
		return answer[0][0]
	else:
		return '(None)'

print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))