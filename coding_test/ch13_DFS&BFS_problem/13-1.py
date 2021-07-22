from collections import deque

n,m,k,x = map(int,input().split())

graph =[[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b) #

distance = [-1] * (n+1)

    
def bfs(graph,x):
    
    queue =deque([x])
    
    while queue:
        
        now = queue.popleft() # 현재도시
        
        for next_city in graph[now]: # 다음도시로 거리
            
            if distance[next_city] == -1: # 방문한적 없었던 도시에 대해서만 처리해야 하므로
                
                distance[next_city] = distance[now] + 1
                queue.append(next_city)
                
                
    check = False  # 조건 부합하는 경우가 하나도 없는 경우를 위해 설정
    
    for i in range(1,n+1):
        if distance[i] == k:
            print(i)
            check = True
            
    if check == False:
        
        print(-1)