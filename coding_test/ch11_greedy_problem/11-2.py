s = input() # 문자열 이니까

result = int(s[0])  # 문자열을 숫자로 바꾸는 방법

for i in range(1,len(s)): # len(s) 에는 마지막 줄바꿈이 포함되어 있어서 저렇게 쓰는게 맞다
    
    if int(s[i]) <= 1 or result <= 1:
        result += int(s[i])
        
    else:
        result *= int(s[i])
        
print(result)

