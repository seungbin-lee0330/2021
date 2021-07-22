from itertools import combinations

n,m = map(int,input().split())

house,chicken = [],[] # 집과 치킨가게를 따로 저장하는것이 포인트

for r in range(n):
    
    data = list(map(int,input().split())) # 한 줄씩 입력받음
    
    for c in range(n):
        
        if data[c] == 1:
            house.append((r,c))
            
        elif data[c] == 2:
            chicken.append((r,c))
            
candidates = list(combinations(chicken,m)) # 치킨가게 중 m 개를 뽑는 조합

def get_sum(candidate):
    
    result = 0
    
    for hx,hy in house:
        
        temp = 1e9
        for cx,cy in candidate:
            
            temp = min(temp,abs(hx-cx) + abs(hy-cy))
            
        result += temp
        
    return result

result = 1e9
for candidate in candidates:
    
    result = min(result,get_sum(candidate))
    
print(result)