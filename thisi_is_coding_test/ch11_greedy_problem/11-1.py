# 다시풀기


n = int(input())
data = list(map(int,input().split()))
data.sort()
result = 0
count = 0 # 현재 그룹에 포함된 모험가의 수를 설정하는 것이 핵심이다

for i in data:
    count += 1
    if i <= count:
        result += 1
        count = 0 # count를 0으로 하는 작업 필요        

print(result)