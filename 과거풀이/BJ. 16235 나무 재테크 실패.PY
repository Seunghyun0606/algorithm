# BJ. 16235 나무 재테크
# 봄 / 여름 /가을 / 겨울 순서로 진행해야함.
# 나무 양분 map, 나무 나이 3차원으로 적립.
# 시간제한있음.
# n 땅크기, m은 나무 갯수 k는 년도
# 2, 3차원을 하나의 배열에 넣으니깐 너무 오래걸리는데 그냥 2차원을 나눠서 하는게 빠를듯

from collections import deque

def summer(x1, y1, i1):
    temp = 0
    while temp < i1 + 1:
        lands[x1][y1][0] += (lands[x1][y1][1].popleft())//2
        temp += 1


def falls(x1, y1):
    dx = [0, 0, 1, -1, 1, -1, 1, -1]
    dy = [1, -1, 0, 0, -1, 1, 1, -1]

    for i2 in range(8):
        row = x1 + dx[i2]
        col = y1 + dy[i2]

        while n > row > -1 and n > col > -1:
            lands[x][y][1].append(1)
            que.append([row, col])


n, m, k = map(int, input().split())

# 2차원 배열 + 3차원 배열의 형태임. 왼쪽은 뉴트리션, 오른쪽은 나무갯수 및 나이
lands = [ [] for _ in range(n) ]
nutri = [ [] for _ in range(n) ]

for i in range(n):
    for j in map(int, input().split()):
        lands[i].append([j, deque()])
        nutri[i].append(j)

que = []
que2 = []
que3 = []  # 위치정보 (falls)
for _ in range(m):
    x, y, z = map(int, input().split())
    lands[x-1][y-1][1].append(z)
    que.append([x-1, y-1])


# 가을할때 다른 나무에 영향을 줄수 있음. 그걸 해결해야함.

time = 0
while True:

    while que:
        que2.append(que.pop())

    while que2:
        x, y = que2.pop()

        for i in range(len(lands[x][y][1])-1, -1, -1):
            youngest_tree = lands[x][y][1][i]

            if lands[x][y][0] < youngest_tree:
                summer(x, y, i)  # 여기서 양분 늘려줄거임
                break
            lands[x][y][0] -= youngest_tree
            lands[x][y][1][i] += 1
            que.append([x, y])
            if not lands[x][y][1][i] % 5:
                que3.append([x, y])

        # 겨울
        for i in range(n):
            for j in range(n):
                lands[i][j][0] += nutri[i][j]

    # 가을
    while que3:
        x, y = que3.pop()
        falls(x, y)

    time += 1

    if time == k:
        break

result = 0
while que:
    x, y = que.pop()
    result += len(lands[x][y][1])

print(result)

