n = int(input("Pleas input area size:"))
x, y = 1, 1
plan = list(map(str, input("Pleas input your plan for trip:").split()))

arrival = (x, y)

for i in plan:
    if i == 'R':
        if not (y + 1> n):# 검사를 먼저 하고 움직일 것(준한 코멘트)
            y += 1  
       
    elif i == 'L':
        y -= 1
        if y == 0:
            y += 1
    elif i == 'U':
        x -= 1
        if x == 0:
            x += 1
    elif i == 'D':
        x += 1
        if x > n:
            x -= 1

    else:
        print("you can't use other command")
  
print(x, y)      