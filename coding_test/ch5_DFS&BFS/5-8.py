def dfs(graph, n , visited):
    
    visited[n] = True # 현재 노드를 방문처리
    print(n, end = ' ')
    
    for i in graph[n]: # 해당 노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[i]:
            dfs(graph, i , visited)
            
graph = [
    [], # 0번째 노드
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