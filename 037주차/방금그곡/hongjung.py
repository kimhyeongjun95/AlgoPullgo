def solution(m, musicinfos):
    def change_note(melody):
        if 'A#' in melody:
            melody = melody.replace('A#', 'a')
        if 'C#' in melody:
            melody = melody.replace('C#', 'c')
        if 'D#' in melody:
            melody = melody.replace('D#', 'd')
        if 'F#' in melody:
            melody = melody.replace('F#', 'f')
        if 'G#' in melody:
            melody = melody.replace('G#', 'g')
        return melody

    m = change_note(m)
    answer = ''
    ans_time = 0
    for info in musicinfos:
        start, end, title, melody = info.split(',')
        start_h, start_m, end_h, end_m = map(int, start.split(':') + end.split(':'))
        time = 60 * (end_h - start_h) + (end_m - start_m)
        melody = change_note(melody)
        melody_played = (melody * time)[:time]
        if m in melody_played:
            if time > ans_time:
                ans_time = time
                answer = title
    if answer == '':
        answer = '(None)'
    return answer

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))

# from collections import defaultdict

# def solution(m, musicinfos):
#     music_dict = defaultdict(list)
#     music_title = []
#     for music in musicinfos:
#         tmp = music.split(',')
#         time = (int(tmp[1][:2]) - int(tmp[0][:2])) * 60 + (int(tmp[1][3:]) - int(tmp[0][3:]))
#         title = tmp[2]
#         notes = tmp[3]
#         music_title.append(title)
#         music_dict[title].append(time)
#         music_dict[title].append(title)
#         music_dict[title].append(notes)
    
#     music_true = defaultdict(int)
#     for music in music_title:
#         notes = music_dict[music][2]
#         tmp = notes * len(m)
#         if m in tmp:
#             if len(m) == len(tmp):
#                 music_true[music] = 1
#             else:
#                 idx = tmp.index(m)
#                 if tmp[idx + len(m)] != '#':
#                     music_true[music] = 1
#                 else:
#                     music_true[music] = 0
#         else:
#             music_true[music] = 0

#     answer = ''
#     time = 0
#     for music in music_title:
#         if music_true[music] and music_dict[music][0] > time:
#             time = music_dict[music][0]
#             answer = music
#     if answer == '':
#         answer = '(None)'
#     return answer