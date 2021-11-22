col, row = map(int, input().split())
area = [[*map(int, input().split())] for _ in range(col)]
# direction = {'up': [-1, 0], 'down': [1, 0], 'right': [0, 1], 'left': [0, -1]}
direction_idx = ['up', 'down', 'right', 'left']
camera = []
copy_area = [[0]*row for _ in range(col)]
for i in range(col):
    for j in range(row):
        if 1 <= area[i][j] <= 5:
            camera.append((i, j, area[i][j]))

first_camera = [['up'],
                ['down'],
                ['right'],
                ['left']]

second_camera = [['up', 'down'],
                 ['right', 'left']]

third_camera = [['up', 'right'],
                ['down', 'right'],
                ['down', 'left'],
                ['up', 'left']]

forth_camera = [['up', 'down', 'right'],
                ['up', 'down', 'left'],
                ['up', 'right', 'left'],
                ['down', 'right', 'left']]

fifth_camera = [['up', 'down', 'right', 'left']]

length = len(camera)
camera_list = []
for i in camera:
    if i[2] == 1:
        camera_list.append(first_camera)
    elif i[2] == 2:
        camera_list.append(second_camera)
    elif i[2] == 3:
        camera_list.append(third_camera)
    elif i[2] == 4:
        camera_list.append(forth_camera)
    elif i[2] == 5:
        camera_list.append(fifth_camera)

def change_area(direction, copy, x, y):
    if direction == 'up':
        while True:
            if x - 1 < 0:
                break
            if copy[x-1][y] == 0:
                copy[x-1][y] = 7
            elif copy[x-1][y] == 6:
                break
            x -= 1
    elif direction == 'down':
        while True:
            if x + 1 >= col:
                break
            if copy[x+1][y] == 0:
                copy[x+1][y] = 7
            elif copy[x+1][y] == 6:
                break
            x += 1
    elif direction == 'left':
        while True:
            if y-1 < 0:
                break
            if copy[x][y-1] == 0:
                copy[x][y-1] = 7
            elif copy[x][y-1] == 6:
                break
            y -= 1
    elif direction == 'right':
        while True:
            if y + 1 >= row:
                break
            if copy[x][y+1] == 0:
                copy[x][y+1] = 7
            elif copy[x][y+1] == 6:
                break
            y += 1

answer = col*row
def back(n=0, ans=[0]*length):
    global answer
    if n == length:
        temp = 0
        for i in range(col):
            for j in range(row):
                copy_area[i][j] = area[i][j]
        for i in range(length):
            for j in range(len(ans[i])):
                    change_area(ans[i][j], copy_area, camera[i][0], camera[i][1])
        for i in range(col):
            for j in range(row):
                if copy_area[i][j] == 0:
                    temp += 1
        if answer > temp:
            answer = temp
        return
    for i in range(len(camera_list[n])):
        ans[n] = camera_list[n][i]
        back(n+1, ans)
        ans[n] = 0

back()
print(answer)