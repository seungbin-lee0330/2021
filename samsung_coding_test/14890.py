# 도저히 아이디어조차 모르겠다
import sys
input = sys.stdin.readline

def check(line):
    check = [False for i in range(n)] # i번째 칸에 경사로를 설치했는지 체크
    for i in range(n - 1):
        if line[i] == line[i + 1]:
            continue
        if abs(line[i] - line[i + 1]) > 1:
            return False
        if line[i] == line[i + 1] + 1: # 경사로 내려가는 경우
            temp = line[i + 1]
            for j in range(i + 1, i + 1 + l): # 경사로의 길이 l만큼 비교
                if 0 <= j < n:
                    if line[j] != temp: return False
                    if check[j] == True: return False # 없어도 된다
                    check[j] = True
                else:
                    return False
        else:
            temp = line[i]
            for j in range(i, i - l, -1):
                if 0 <= j < n:
                    if line[j] != temp: return False
                    if check[j] == True: return False # 내려가는 경사로와 겹치는 경우 제외처리
                    check[j] = True
                else:
                    return False
    return True
n, l = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
cnt = 0
for i in s:
    if check(i):
        cnt += 1
for i in range(n): # transpose 하는 방법 # rotate 90 이랑 다르다
    tmp = []
    for j in range(n):
        tmp.append(s[j][i])
    if check(tmp):
        cnt += 1
print(cnt)