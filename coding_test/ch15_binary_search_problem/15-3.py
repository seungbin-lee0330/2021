# 어렵다

n,c = map(int,input().split())
houses = []
for i in range(n):
    houses.append(int(input()))
houses.sort()

start = 1   # 가능한 최소 거리
end = houses[-1] - houses[0] # 가능한 최대 거리
result = 0

while start <= end:
    mid = (start+end) // 2
    value = houses[0]
    count = 1 
    for i in range(1,n): # 앞에서부터 차근차근 설치
        if houses[i] >= value + mid:
            value = houses[i]
            count += 1
    if count >= c: # c개 이상의 공유기를 설치할 수 있는 경우
        start = mid + 1
        result = mid
    else:
        end = mid - 1
        
print(result)
                     