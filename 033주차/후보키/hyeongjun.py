# 프로그래머스 후보키

# 유일성 : 모든 튜플에 대해 유일하게 식별
# uniqueness
# 최소성 : 유일성을 가진 속성 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미
#          릴레이션의 모든 튜플을 유일하게 식별하는데 꼭 필요한 속성들로만 구성되어야 함
# minimality

# 학번, [이름, 전공]
# 후보 키의 개수 return

from itertools import combinations
def solution(relation):
    
    m = len(relation[0])

    result = []
    for i in range(1, m+1):
        for combo in combinations(range(m), i):

            check = []
            for rel in relation:
                temp = [rel[c] for c in combo]
                # 유효성 확인
                if temp in check:
                    break
                check.append(temp)
            else:
                for ck in result:
                    # 최소성 확인 
                    if set(ck).issubset(set(combo)):
                        break
                else:
                    result.append(combo)

    answer = len(result)
    return answer



print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
# 2
