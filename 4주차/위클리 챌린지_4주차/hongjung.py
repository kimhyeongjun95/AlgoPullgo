# 직업군 추천하기

def solution(table, languages, preference):
    scores = [] # [[직업군, 최종점수], [] ....] 이렇게 입력
    for i in table:
        tmp_sum = 0 # 최종점수
        tmp_list = list(map(str, i.split())) # 각 요소를 다시 리스트로 변환
        multiply = [5, 4, 3, 2, 1] # 직업군 언어 점수
        for j in range(len(languages)):
            for k in range(len(tmp_list[1:])): # 직업군을 제외한 그 뒤의 리스트 요소들로
                if languages[j] == tmp_list[1:][k]: # 만약 languages의 언어와 같다면
                    tmp_sum += preference[j] * multiply[k] # 그 언어의 선호도와 리스트 요소의 직업군 언어 점수를 곱하여 최종 점수 산출
        scores.append([tmp_list[0], tmp_sum]) # [직업군, 최종점수]로 scores에 추가
    
    max_sum = scores[0][1] # 가장 높은 최종점수 구해주기
    for i in range(5):
        if scores[i][1] > max_sum:
            max_sum = scores[i][1]
    
    max_list = []
    for i in range(5): # 가장 높은 최종점수를 얻은 직업군들을 리스트에 추가
        if scores[i][1] == max_sum:
            max_list.append(scores[i][0])
    
    max_list.sort() # 직업군을 오름차순을 정렬
    answer = max_list[0] # 정렬 후 가장 앞에 있는 직업군을 반환
    return answer