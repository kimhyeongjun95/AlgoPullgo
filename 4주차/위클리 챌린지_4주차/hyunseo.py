def solution(table, languages, preference):
    new_table = []
    for row in table:
        new_table.append(row.split())
    
    total = [0]*5  # SI, CONTENTS, HARDWARE, PORTAL, GAME

    # table에 적용할 인덱스 0~4
    # 0:SI, 1:CONTENTS, 2:HARDWARE, 3:PORTAL, 4:GAME
    for i in range(5):

        # languages에 적용할 인덱스
        for j in range(len(languages)):

            # tabel[i]의 언어에 적용할 인덱스 1~5
            # 1 : 5점언어, 2 : 4점언어, ... 5 : 1점언어
            for k in range(1, 6):

                if new_table[i][k] == languages[j]:
                    total[i] += (6-k)*preference[j]
                    break

    answer = []
    for l in range(5):
        if total[l] == max(total):
            answer.append(new_table[l][0])

    answer.sort()

    return answer[0]

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
pre = [7, 5, 5]

print(solution(table, languages, pre))