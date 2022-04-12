# 프로그래머스 방금그곡

# return 음악의 제목

# C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개
# 1분에 1개씩 재생
# 반드시 처음부터 재생
# 길이보다 재생된 시간이 길 때는 음악이 끊김없이 처음부터 반복해서 재생
# 조건 만족 여러개 : 재생된 시간이 제일 긴 음악 return
# 재생된 시간도 같으면 먼저 입력된 음악 반환
# 조건 X : (None) 반환

# m : 네오가 기억한 멜로디를 담은 문자열
# musicinfos : 방송된 곡의 정보를 담고 있는 배열
# 시작시간, 끝난시간, 음악제목, 악보정보

# 1. musicinfos에 따라 실제 들린음악 문자열 만들기
# 1-1 "#"달린 음 확인
# 2. 거기에 m이 있는지 확인
# 2-1. 제일 긴 음악 return
# 2-2. 먼저 입력된 음악 return
# 2-3. 없으면 None return

def solution(m, musicinfos):

    result = []
    count = 1
    for mi in musicinfos:
        st, et, title, info = mi.split(',')
        sh, sm = st[:2], st[3:]
        eh, em = et[:2], et[3:]
        total_s = int(sh) * 60 + int(sm)
        total_e = int(eh) * 60 + int(em)
        time = total_e - total_s
        
        # 1
        length = len(info)
        temp = ''
        idx = 0
        for _ in range(time):
            # 1-1
            e_idx = (idx+1) % length
            if info[idx%length] + info[e_idx] in ['C#', 'D#', 'F#', 'G#', 'A#']:
                temp += info[idx%length] + info[e_idx]
                idx += 2
            else:
                temp += info[idx % length]
                idx += 1

        # 2
        long = len(m)
        for i in range(len(temp)-long+1):
            # 샵 있으면 안됌..
            if m[-1] != '#' and temp[(i+long) % len(temp)] == '#':
                continue
            if m == temp[i:i+long]:
                # 2-1, 2-2를 위해
                result.append((title, time, count))
                break
        
        # 2-2
        count += 1

    # 2-3
    if not result:
        return "(None)"
    
    # 2-1, 2-2
    result.sort(key = lambda x : (-x[1], x[2]))
    return result[0][0]

# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# HELLO
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# "FOO"
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# "WORLD"

