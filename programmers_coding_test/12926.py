def caesar(s, n):
    s = list(s) # 리스트로 바꿔서 값을 수정한다!!
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A')) # 나머지를 사용한 표기법
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))
    return "".join(s)