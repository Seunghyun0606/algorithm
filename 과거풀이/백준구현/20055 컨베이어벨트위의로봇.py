from collections import deque
n, k = map(int, input().split())

belts = deque(list(map(lambda x: [x, 0], map(int, input().split()))))

cnt = 0
time = 0
# 내구도, 로봇유무, 위치
while cnt < k:
    
    belts.appendleft(belts.pop())
    
    if belts[n-1][1]:
        belts[n-1][1] = 0
    for i in range(n-2, 0, -1):
        durabilty, robot = belts[i]
        if robot:
            next_durability, next_robot = belts[i+1]
            if next_durability and not next_robot:
                belts[i] = [durabilty, 0]
                belts[i+1] = [next_durability - 1, 1]
                if next_durability == 1:
                    cnt += 1
    else:
        if belts[n-1][1]:
            belts[n-1][1] = 0
    if belts[0][0]:
        belts[0][0] -= 1
        belts[0][1] = 1
        if not belts[0][0]:
            cnt += 1
    time += 1
else:
    print(time)

        

