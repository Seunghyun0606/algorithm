# BJ. 2636 치즈
# BFS로 풀어보자.
# 공기를 바꾸는 것으로 치즈 안쪽 부분을 해결함.


from collections import deque


def melting(removing):
    cnt = 0
    que = deque()
    que.append([0, 0])
    cheese[0][0] = removing

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while que:
        x, y = que.popleft()

        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]
            if n > row > -1 and m > col > -1:
                if cheese[row][col] == removing:
                    continue
                elif cheese[row][col] == 1:  # 외곽 치즈
                    cheese[row][col] = removing
                    cnt += 1
                else:  # 0일때 (공기)
                    cheese[row][col] = removing
                    que.append([row, col])

    return cnt


n, m = map(int, input().split())

cheese = [[ i for i in map(int, input().split())] for _ in range(n)]

time = 0
count = n*m

while True:
    time -= 1
    temp = melting(time)
    if temp == 0:
        break
    count = min(temp, count)

print((time+1)*(-1))
print(count)
