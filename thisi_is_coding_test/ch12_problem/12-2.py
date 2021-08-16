# s = input() 
# answer = '' ### 문자열로 풀기 어렵네 sort 같은 문자열을 정렬하는 방법이 없어서!!!
# sum = 0

# for i in s:
#     if i.isalpha():
#         answer += i
#     else:
#         sum += int(i)
# answer = sorted(answer) 
# if sum != 0:
#     answer += str(sum)
# print(answer)







# s = input()
# answer = []
# sum = 0

# for i in s:
#     if i.isalpha():              # .isalpha() 이렇게 쓴다 반환값은 True or False
#         answer.append(i)
#     else:
#         sum += int(i)
# answer.sort()
# answer = "".join(answer)
# if len(answer) != len(s): # 이렇게 써야 0만 있는경우도 잡아내지 않을까!
#     answer += str(sum)
# print(answer)



















# s = input()
# result =[] #sort를 위해 리스트를 사용한다
# sum = 0

# for i in s:
#     if i.isalpha(): # 문자열이 알파벳인지 확인 여러개여도 모두 확인가능하고 숫자확인을 위해서는 .isdigit() 을 사용한다.
#         result.append(i)
#     else:
#         sum += int(i)
# result = sorted(result)
# if sum != 0: # 숫자가 하나라도 있는 경우
#     result.append(str(sum)) # 문자열로 넣어주어야 나중에 join으로 합치는게 가능
    
# print(''.join(result))
