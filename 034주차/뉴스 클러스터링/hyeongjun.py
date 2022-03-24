# 프로그래머스 [1차] 뉴스 클리스터링

# 유사한 기사를 묶는 기준 -> 자카드 유사도
# 자카드 유사도 : (A, B) 두 집합의 교집합 크기 / 두 집합의 합집합 크기

# A = {1, 2, 3}
# B = {2, 3, 4}
# A ∩ B = {2, 3}
# A ∪ B = {1, 2, 3, 4}
# J(A, B) = 2 / 4 = 0.5
# 모두 공집합? => J(A, B) = 1

# "FRANCE", "FRENCH"
# {FR, RA, AN, NC, CE}, {FR, RE, EN, NC, CH}
# 교집합 : {FR, NC}
# 합집합 : {FR, RA, AN, NC, CE, RE, EN, CH}
# J("FRANCE", "FRENCH") = 2/8 = 0.25

# A = {1, 1, 2, 2, 3}
# B = {1, 2, 2, 4, 5}
# A ∩ B = {1, 2, 2} : min(2)
# A ∪ B = {1, 1, 2, 2, 3, 4, 5} : max(1)

# 두 글자, (공백, 숫자, 특수 문자) 버리기

# return 유사도 x 65536 하고 소수 버리기

# 1. 각각 2개씩 끊기
#   1-1. 알파벳 제외 버리기
#   1-2. 모두 공집합이면 return 1
# 2. 교집합 구하기
#   2-1. 교집합 요소 각각 문자열에서 count해서 min 갯수만큼 length +=
# 3. 합집합 구하기
#   3-1. 합집합 요소 각각 문자열에서 count해서 max 개수만큼 length +=

def solution(str1, str2):

    s1 = ''
    for i in str1:
        if i.upper():
            s1 += i.lower()
        else:
            s1 += i
    
    s2 = ''
    for i in str2:
        if i.upper():
            s2 += i.lower()
        else:
            s2 += i

    # 1
    s1_set = []
    for i in range(len(s1)-1):
        temp = s1[i:i+2]
        # 1-1
        flag = False
        for j in temp:
            if j == ' ' or j.isdigit() or not j.isalpha():
                flag = True
                break
        if flag:
            continue
        s1_set.append(temp)
    
    # 1
    s2_set = []
    for i in range(len(s2)-1):
        temp = s2[i:i+2]
        # 1-1
        flag = False
        for j in temp:
            if j == ' ' or j.isdigit() or not j.isalpha():
                flag = True
                break
        if flag:
            continue
        s2_set.append(temp)

    # 1-2
    if len(s1_set) == 0 and len(s2_set) == 0:
        return 65536
    
    # 2
    inter = list(set(s1_set).intersection(s2_set))
    inter_count = 0
    for i in inter:
        # 2-1
        count = min(s1_set.count(i), s2_set.count(i))
        inter_count += count
    
    # 3
    unioned = list(set().union(s1_set, s2_set))
    unioned_count = 0
    for i in unioned:
        # 3-2
        count = max(s1_set.count(i), s2_set.count(i))
        unioned_count += count
    
    similarity = inter_count / unioned_count
    answer = int(65536 * similarity)

    return answer

print(solution("FRANCE", "french"))
# 16384
print(solution("handshake", "shake hands"))
# 65536
print(solution("aa1+aa2", "AAAA12"))
# 43690
print(solution("E=M*C^2", "e=m*c^2"))
# 65536