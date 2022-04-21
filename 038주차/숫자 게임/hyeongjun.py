# 프로그래머스 숫자 게임

def solution(A, B):
	A.sort()
	B.sort()
	j = 0
	answer = 0
	for i in range(len(B)):
		if A[j] < B[i]:
			j += 1
			answer += 1
	return answer
			

print(solution([5,1,3,7], [2,2,6,8]))
# 3
print(solution([2,2,2,2], [1, 1, 1, 1]))
# 0