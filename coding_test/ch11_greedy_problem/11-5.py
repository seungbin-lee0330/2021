n,m = map(int,input().split())

weight = list(map(int,input().split()))

count = 0

for i in range(n):
    for j in range(1,n-i):
    
        if weight[i] != weight[i+j]:
            count += 1
            
print(count)