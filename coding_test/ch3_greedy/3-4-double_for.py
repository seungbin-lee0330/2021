



























n,m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int,input().split()))
    
    min_value = 10001
    
    for j in data:
            min_value = min(min_value,j) # 굳이 이렇게 할 필요가 있을까 그냥 연습하는거지 더 비효율적인거 같음
             
    result = max(result, min_value)
    
print(result)