# 프로그래머스 N-Queen

def diagonalPass(row, col):
	for i in range(row):
		# 행과 열의 차이가 같다면 동일 대각선에 있음
		if row - i == abs(col-arr[i]):
			return False
	return True

def check(idx, n):
	global answer, visited, arr

	if idx == n:
		answer += 1
		print(arr, visited)
		return

	for i in range(n):
		# col / diagonal 체크
		if not visited[i] and diagonalPass(idx, i):
			visited[i] = 1 # 열 표시
			arr[idx] = i # 열 표시
			check(idx+1, n)
			visited[i] = 0

def solution(n):
	global answer, visited, arr
	answer = 0
	arr = [0] * n
	visited = [0] * n
	check(0, n)
	return answer

print(solution(4)) # 2