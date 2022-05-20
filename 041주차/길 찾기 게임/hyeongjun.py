# 프로그래머스 (2019 카카오) 길 찾기 게임

# 두 팀으로 나누고, 각 팀이 같은 곳을 다른 순서로 방문하도록
# 먼저 순회를 마친 팀이 승리

# 각 장소를 이진트리의 노드가 되도록 구성
# 순회 방법을 힌트로 주어 각 팀이 스스로 경로를 찾도록

# 모든 노드는 서로 다른 x
# 같은 레벨에 있는 노드는 같은 y
# 부모 y > 자식 y
# V의 x > left subtree의 x
# V의 x < right subtree의 x

# 이진트리를 구성하는 노드들의 좌표: nodeinfo
# 전위 순회, 후위 순회 결과 return

# 이진트리 어떻게 만들지?

def pre_order(arr, result_pre):
	node = arr[0]
	arr1 = []
	arr2 = []

	for i in range(1, len(arr)):
		# x보다 작은 (왼쪽)
		if node[0] > arr[i][0]:
			arr1.append(arr[i])
		else:
			arr2.append(arr[i])

	result_pre.append(node[2])
	# 제일 자식이 아니라면
	if len(arr1):
		pre_order(arr1, result_pre)
	if len(arr2):
		pre_order(arr2, result_pre)

def post_order(arr, result_post):
	node = arr[0]
	arr1 = []
	arr2 = []

	for i in range(1, len(arr)):
		# x보다 작은 (왼쪽)
		if node[0] > arr[i][0]:
			arr1.append(arr[i])
		else:
			arr2.append(arr[i])

	# 제일 자식이 아니라면
	if len(arr1):
		post_order(arr1, result_post)
	if len(arr2):
		post_order(arr2, result_post)
	result_post.append(node[2])

def solution(nodeinfo):

	for i in range(len(nodeinfo)):
		nodeinfo[i].append(i+1)

	result_pre = []
	result_post = []

	arr = sorted(nodeinfo, key = lambda x: (-x[1], x[0]))
	print(arr)
	pre_order(arr, result_pre)
	post_order(arr, result_post)

	return [result_pre, result_post]

print(solution(
	[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	
))
# [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
