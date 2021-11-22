# BJ. 11967 불켜기
# 방에 들어가면 버튼을 다 켜 그런다음 buttons는 pop해서 빈리스트 만든다(visit 역할) -> 안됨. visit새로만들어야함
# 왜냐면 스위치 없는 방이지만 불이켜져있어서 지나가면 스위치있는방으로도 갈 수 있기 때문.
# 그런다음에 갈수있는 곳은 que에 넣는다.
# 불을킬때마다 1을 적립한다(중복안됨)

from collections import deque

n, m = map(int, input().split())

buttons = [ [ [] for _ in range(n)] for _ in range(n) ]

for _ in range(m):
    x, y, a, b = map(int, input().split())
    buttons[x-1][y-1].append([a-1, b-1])

status = [ [0]*n for _ in range(n) ]
visit = [ [0]*n for _ in range(n)]

que = deque()
que2 = deque()
que.append([0, 0])
status[0][0] = 1
visit[0][0] = 1
count = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while que:
    x, y = que.popleft()

    while buttons[x][y]:  # 현재위치의 버튼부터 일단 킨다음에 움직인다.
        x1, y1 = buttons[x][y].pop()
        if status[x1][y1] == 0:
            status[x1][y1] = 1
            count += 1
            que2.append([x1, y1])

    # 불켰으니 이동해보자
    # 불킨 곳을 기준으로 4방향에서 하나로도 불이켜져있고, 이전에 방문한데가 있다면,
    # 불킨 곳을 visit했다고하고 que에 넣어준다.
    while que2:
        x, y = que2.pop()

        for i in range(4):
            row = x + dx[i]
            col = y + dy[i]

            if n > row > -1 and n > col > -1 and visit[row][col] and status[row][col]:
                visit[x][y] = 1
                que.append([x, y])
                break


print(count)
print(*status, sep='\n')
