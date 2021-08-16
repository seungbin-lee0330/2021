f = open("9-3.txt")
input = f.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 리스트 모두 무한으로 초기화

for a in range(1, n+1): # 대각 성분 모두 0으로 초기화, 자기 자신으로 가는 비용이므로
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
    
for _ in range(m):
    
    a,b,c = map(int,input().split())
    graph[a][b] = c
    
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])
            
for a in range(1,n+1):
    for b in range(1,n+1):
        
        if graph[a][b] == INF:
            print("INFINITY", end= " ")
            
        else:
            print(graph[a][b], end = " ")
            
    print() # 줄 바꿈