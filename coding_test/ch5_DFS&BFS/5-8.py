def dfs(graph, n , visited): # 깊이 우선 탐색, Depth=First Search
    
    visited[n] = True # 현재 노드를 방문처리
    print(n, end = ' ') # 줄바꿈 없이 계속 출력하기 위해서 사용
    
    for i in graph[n]: # 해당 노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            dfs(graph, i , visited) # dfs는 재귀함수로 구현함을 기억하자
            
graph = [
    [], # 0번째 노드 인덱스 맞춰주기 위해 삽입
    [2,3,8], # 1번째 노드
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

dfs(graph,1,visited)