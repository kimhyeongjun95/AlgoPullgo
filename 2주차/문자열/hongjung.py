import sys

A, B = sys.stdin.readline().split()

difference = len(B) - len(A) # 문자열 A와 B의 길이 차이를 구함

result = 50 # 두 문자열의 최대 길이는 50이므로 최대 50만큼 차이가 있음

for i in range(difference+1): # 차이에 +1 만큼 반복, 예를 들어 abcd ab가 있다면 ab와 ab, ab와 bc, ab와 cd 이렇게 두 문자열 사이의 길이 차이는 2번이지만 비교는 3번함
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[i:][j]: # B 문자열의 인덱스를 하나씩 뒤로 밀면서 A 문자열과 차이를 비교
            cnt += 1
    if cnt < result:
        result = cnt # 차이가 가장 작은 값을 결과값으로

print(result)