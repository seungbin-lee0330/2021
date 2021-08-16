# 문제 잘 읽고 다시풀기


n = int(input())

houses = list(map(int,input().split()))
houses.sort()

print(houses[(n+1)//2 - 1]) # 중간값중 작은 인덱스가 항상 답이닫
