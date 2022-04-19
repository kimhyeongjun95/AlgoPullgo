T=int(input())
for _ in range(T):
    N=int(input())
    parent=[0 for _ in range(N+1)]
    for _ in range(N-1):
        parent_indi,child=map(int,input().split())
        parent[child]=parent_indi#부모 노드 저장
 
    a,b=map(int,input().split())
    a_parent=[a]
    b_parent=[b]
    #각노드의 부모노드가 루트일때까지 모두 저장
    while parent[a]:
        a_parent.append(parent[a])
        a=parent[a]
 
    while parent[b]:
        b_parent.append(parent[b])
        b=parent[b]
 
 
    # 몇층에 있는지
    len_a = len(a_parent)-1
    len_b = len(b_parent)-1

    while True:
        if a_parent[len_a] == b_parent[len_b]:
            len_a -= 1
            len_b -= 1
        else:
           break
 
    print(a_parent[len_a+1])

    # 근데 처음에 내가 26번째줄에
    #  if a_parent[len_a] == b_parent[len_b]:
        # if len_a > 0:
            # len_a -= 1
        # if len_b > 0:  
            # len_b -= 1
    # 햇는데 런타임에러뜸
    # 왜이런교?