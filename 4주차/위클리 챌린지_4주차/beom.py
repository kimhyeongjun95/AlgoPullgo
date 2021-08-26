table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]

def solution(table, languages, preference):
    answer = ''
    result = []
    table = [i.split() for i in table]
    lang_prefer = dict(zip(languages, preference))
    

    for type in table:
        scores = []
        for lan_type in range(1, len(type)):
            if type[lan_type] in languages:
                score = (len(type)-lan_type) * lang_prefer[type[lan_type]]
                scores.append(score)
            
        result.append((type[0], sum(scores)))
    answer = sorted(result, key=lambda x: (-x[1], x[0]))
    print(answer)
    return answer[0][0]

print(solution(table, languages, preference))

