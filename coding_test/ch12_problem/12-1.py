n = input()

h = len(n) // 2
left = 0
right = 0


for i in range(h):
    
    left += int(n[i])
    right += int(n[h+i])

if left == right:
    print("LUCKY")
    
else:
    print("READY")