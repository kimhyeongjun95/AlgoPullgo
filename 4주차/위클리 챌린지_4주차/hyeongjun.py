def solution(table, languages, preference):
    # preference x table이 가장 높은 직업군 return
    # preference : 언어 선호도
    # table : 직업군 언어 점수 // N x N 리스트가 아닌 문자열!!!
    # languages : 개발자가 사용하는 언어를 담은 문자열 배열
    
    person = {}
    for i, j in zip(languages, preference):
        person[i] = j
    
    temp = []
    for i in table:
        i = i.split(' ') # 처음 i는 ['SI', 'JAVA', 'JAVASCRIPT', 'SQL', 'PYTHON', 'C#']
        score = []
        # print(i)
        for j in range(1, len(i)): # 처음 'SI'를 제외한 언어들을 탐색
                if i[j] in person: # person이 요구하는 언어를 사용한다면 // 3번 활성화 될거임 // SI에서 처음 i[j]는 SQL
                    score.append(person[i[j]] * (6-j)) # 5, 4, 3, 2, 1을 얻어야함 // j는 1, 2, 3, 4, 5
        temp.append((i[0], sum(score)))
    
    # print(temp)
    answer = sorted(temp, key = lambda x : (int(-x[1]), x[0])) # 점수를 기준으로 역순정렬 // 점수가 동일하면 이름순 // reverse=True 대신 -를 써도 된다.
    # print(answer)
    return answer[0][0]

        
# table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
# languages = ["PYTHON", "C++", "SQL"]
# preference = [7, 5, 5]
# return : HARDWARE

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]
print(solution(table, languages, preference))