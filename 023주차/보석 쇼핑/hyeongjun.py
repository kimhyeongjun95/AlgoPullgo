# 프로그래머스 보석 쇼핑
def solution(gems):
    answer = [] 
    shortest = len(gems)

    left = 0 
    right = 0 

    length = len(set(gems)) 
    contained = {} 

    while right < len(gems): 

        if gems[right] not in contained: 
            contained[gems[right]] = 1 
        else:
            contained[gems[right]] += 1 
        right += 1 # 테케 3번
        
        if len(contained) == length: # 다 들어감
            while left < right: # 만나기 전까지
                if contained[gems[left]] > 1: # 2개 이상
                    contained[gems[left]] -= 1 
                    left += 1 
                elif shortest > right - left: 
                    shortest = right - left
                    answer = [left+1, right] 
                    break 
                else:
                    break

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])) # [3, 7]