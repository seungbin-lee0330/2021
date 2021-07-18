# 다시풀기


s = input()

result =[] #sort나 원소추가의 용이성을 위해 리스트를 사용한다
sum = 0

for i in s:
    
    if i.isalpha(): # 문자열이 알파벳인지 확인 여러개여도 모두 확인가능하고 숫자확인을 위해서는 .isdigit() 을 사용한다.
        result.append(i)
        
    else:
        sum += int(i)

result = sorted(result)
        
if sum != 0: # 숫자가 하나라도 있는 경우
    
    result.append(str(sum)) # 문자열로 넣어주어야 나중에 변환이 가능
                  
print(''.join(result))