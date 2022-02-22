# 프로그래머스 삼각 달팽이

# 반 시계방향으로 달팽이 채우기 진행

def solution(n):
	result = [[0] * n for _ in range(n)]
	x, y = -1, 0 # 처음 꺾기 전
	count = 1

	for i in range(n):
		for _ in range(i, n):
			if i % 3 == 0:
				x += 1

			elif i % 3 == 1:
				y += 1
			
			elif i % 3 == 2:
				x -= 1
				y -= 1
			
			result[x][y] = count
			count += 1
	answer = []
	for i in result:
		for j in i:
			if j:
				answer.append(j)

	return answer

print(solution(4))
# [1,2,9,3,10,8,4,5,6,7]
print(solution(5))
# # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
print(solution(6))
# # [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]