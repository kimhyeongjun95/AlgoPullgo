# 프로그래머스 단속카메라

# 차량의 경로 routes
# 모든 차량이 한 번은 단속용 카메라를 만나도록
# 최소 몇 대의 카메라를 설치해야 하는지?

# [0] 진입한 지점 [1] 나간 지점


def solution(routes):
	routes.sort(key=lambda x: x[1])
	# [[-20, -15], [-18, -13], [-14, -5], [-5, -3]]
	answer = 1
	now = routes[0][1]

	for i in range(1, len(routes)):
		if now < routes[i][0]:
			now = routes[i][1]
			answer += 1
	
	return answer


print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	))
# 2
