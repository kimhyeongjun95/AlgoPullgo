def solution(s):
    answer = []
    s = s[1:-2]    
    s = s.split('},')
    
    result = []
    for i in s:
        temp = i[1:]
        result.append(list(map(int, temp.split(','))))
    
    # 작은 값부터 튜플의 순서대로 들어가기 때문에 길이 순서대로 정렬
    result = sorted(result, key=lambda x: len(x))
    
    # 다음값이랑 이전값을 set을 이용해서 중복 제거한다.
    temp = set()
    for i in result:
        num = list(set(i)-temp)
        answer.append(num[0])
        temp = set(i)
        
    return answer
