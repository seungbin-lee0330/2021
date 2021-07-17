def find_parent(parent,x): # 경로 압축 기법 소스코드
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
        
    return parent[x]