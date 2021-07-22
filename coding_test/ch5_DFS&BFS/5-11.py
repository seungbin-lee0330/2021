
























# from collections import deque

# n,m = map(int,input().split())

# graph =[]

# for i in range(n):
#     graph.append(list(map(int,input())))
    
# dx = [-1,1,0,0] # 좌 우 하 상
# dy = [0,0,-1,1]

# def bfs(x,y):
    
#     queue = deque()
#     queue.append((x,y))
    
#     while queue:
#         x, y = queue.popleft()
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if nx < 0 or ny < 0 or nx >= n or ny >= m: # 공간 벗어나는 경우
#                 continue
            
#             if graph[nx][ny] == 0: # 벽인 경우
#                 continue
            
#             if graph[nx][ny] == 1: # 첫방문인 경우에만
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx,ny))
                
#     return graph[n-1][m-1] # 가장 오른쪽 아래 최단거리 반환

# print(bfs(0,0))