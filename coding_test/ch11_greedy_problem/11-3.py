# 다시풀어보기

# 직관적인 풀이방법

data = input()

count0 = 0 # 전부 0으로 바꾸는 방법
count1 = 0 # 전부 1로 바꾸는 방법

if data[0] == '0':
    count1 += 1
    
else :
    count0 += 1
    
for i in range(1,len(data)-1):
    
    if data[i] != data[i+1]:
        if data[i+1] == 0:
            count1 += 1
        else:
            count0 += 1
            
print(min(count0,count1))














# 내 풀이지만 알아보기 힘들다
# s = input()

# result = 0

# for i in range(len(s)-1):
    
#     if int(s[i]) != int(s[i+1]):
#         result += 1
        
# print((result+1)//2)