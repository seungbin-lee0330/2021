n,m = map(int,input().split()) # n은 화폐의 개수, m은 금액

array =[]

for i in range(n):
    array.append(int(input()))
    
d = [10001] * (m + 1) # 10001은 계산불가를 의미하고 m + 1 을 한 이유는 0원부터 시작했으므로 배열 개수가 하나 더 있어야함

d[0] = 0

for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1) # 최솟값을 찾기위한 테크닉
            
            
if d[m] == 10001:
    print(-1)
    
else:
    print(d[m])

