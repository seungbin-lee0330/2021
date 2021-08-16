f = open("9-1.txt")
input = f.readline

import sys
#input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())

start = int(input())

graph = [[] for i in range(n+1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기

visited = [False] * (n+1)

distance = [INF] * (n+1)

for _ in range(m): # 모든 간선 정보를 입력받기
    
    a,b,c = map(int,input().split()) # a번 노드에서 b번 노드로 가는 비용이 c라는 뜻
    graph[a].append((b,c))
    
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
        
    return index

def dijkstra(start):
    
    distance[start] = 0 # 시작 노드 초기화
    visited[start] = True
    
    for j in graph[start]:
        distance[j[0]] = j[1] # 튜플 0번째에 저장된 노드 값으로 가는 거리가 튜플 1번째에 저장되어 있다
        
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        
        for j in graph[now]:
            cost = distance[now] + j[1]
            
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
dijkstra(start)

for i in range(1,n+1):
    
    if distance[i] == INF:
        print("INFINITY")
        
    else:
        print(distance[i])
        
f.close()