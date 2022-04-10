def solution(m, musicinfos):
    answer = '(None)'
    answer_time = 0
    change_list = ['C#', 'D#', 'F#', 'G#', 'A#']
    new_list = ['c', 'd', 'f', 'g', 'a']

    for change, new in zip(change_list, new_list):
        m = m.replace(change, new)

    for musicinfo in musicinfos:
        start, end, title, music = musicinfo.split(',')

        for change, new in zip(change_list, new_list):
            music = music.replace(change, new)
            
        l = len(music)
        s_h, s_m = list(map(int, start.split(":")))
        e_h, e_m = list(map(int, end.split(":")))
        time = (e_h * 60 + e_m) - (s_h * 60 + s_m)
        
        if time <= l:
            result = music[:time]
        else:
            x, y = divmod(time, l)
            result = music * x + music[:y]

        if m in result:
            if answer_time < time:
                answer = title
                answer_time = time
    return answer

m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))