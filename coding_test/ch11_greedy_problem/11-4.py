# 다시풀기 아이디어 생각하기 어려웠다


























n = int(input())
data = list(map(int,input().split()))
data.sort()
target = 1

for i in data:
    if target < i : # 1원부터 계속 확인하는거지
        break
    target += i 
    
print(target)
    
    