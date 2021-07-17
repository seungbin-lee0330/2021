def find_parent(parent,x): # 루트노드 찾기
    
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if a < b:
        parent[b] = a
        
    else:
        parent[a] = b
        
v,e = map(int,input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

for i in range(1,v + 1):
    parent[i] = i # 부모를 자기 자신으로 초기화
    
for i in range(e):
    a,b = map(int, input().split())
    union_parent(parent,a,b)
    
print('각 원소가 속한 집합: ' , end= '') # 띄어쓰기 없이 이어붙이기
for i in range(1, v + 1):
    print(find_parent(parent,i), end=' ')
    
print()

print('부모 테이블: ' , end='')
for i in range(1,v + 1):
    print(parent[i], end=' ')