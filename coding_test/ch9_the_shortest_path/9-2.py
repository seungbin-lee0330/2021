import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
                    
def dijkstra(Start):
    q = []
    
    heapq.heappush(q,(0,start)) # start 즉 시작노드로 가기 위한 최단경로는 0으로 설정한다. 
    # 힙 자료구조는 튜플을 입력받으면 튜플의 첫 번째 원소를 기준으로 우선순위 큐를 구성한다
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
            
        for i in graph[now]:
            cost = dist + i[1] # 2번째 요소인 거리값을 더해준다
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
dijkstra(start)

for i in range(1,n+1):
    
    if distance[i] == INF:
        print("INFINITY")
        
    else:
        print(distance[i])
                
                