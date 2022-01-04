def solution(gems):
    length = len(set(gems))
    start = 0
    end = 0
    have = {gems[0]: 1}
    ans = [1, len(gems)]

    while start < len(gems):

        if len(have) == length:
            if end - start < ans[1] - ans[0]:
                ans = [start + 1, end + 1]
            if have[gems[start]] == 1:
                del have[gems[start]]
            else:
                have[gems[start]] -= 1
            start += 1

        else:
            end += 1
            if end == len(gems):
                break
            if gems[end] in have:
                have[gems[end]] += 1
            else:
                have[gems[end]] = 1
    print(ans)
    return ans


solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])
