# 이전 리스트의 값과 비교하면서, 그 차가 차이날 때(=경사로일 때) 문제의 조건을 만족하는지 하지않는지 판별
# 먼저 값이 차이날 때 -> 값의 차가 1일때(2 이상이면 경사로를 놓을 수 없음) -> 경사로가 놓이는 자리의 길이 평지일 때 를 확인함


N, L = map(int, input().split())
field = []

for i in range(N):

    arr = [int(x) for x in input().split()]
    field.append(arr)

cnt = 0

for i in range(N):  # 가로
    j = 1
    flag = True
    path = [1] * (N+1)  # 이미 경사로 놓은 자리 visit 표시해주는 리스트
    while True:
        if j >= N:
            break
        if field[i][j-1] != field[i][j]:  # 만약 경사로이면
            if abs(field[i][j-1] - field[i][j]) >= 2:  # 높이가 2 이상 차이나면 어차피 못하므로 Break
                flag = False
                break
            else:
                lth = 1
                if field[i][j-1] - field[i][j] > 0:  # 내리막길일때
                    while lth < L:
                        if j + lth >= N or path[j+lth] == 0:  # 범위 벗어나거나 이미 경사로 놓은거면
                            flag = False
                            break
                        if field[i][j] != field[i][j+lth]:  # 만약 경사로 놓는 곳 범위 내에 높이가 다르면 못놓으므로
                            flag = False
                            break
                        else:
                            path[j+lth-1] = 0  # 방문한데 표시
                        lth += 1
                    if flag == True:
                        if L == 1:  # 경사로 L = 1
                            j += 1
                        else:       # 여기가 틀림. j += 1이아니라 j += lth 되어야하고, path[j-1] 을 0으로만들어줘야함.
                            j += lth
                            path[j-1] = 0
                    else:
                        break
                else:  # 오르막길
                    lth = -1
                    if L == 1:  # 경사로 L = 1 일떄
                        if j-2 >= 0 and field[i][j-2] == field[i][j]:  # 경사로 놓는데가 겹치는 구간인지 확인
                            flag = False
                    else:
                        while abs(lth) < L:
                            if j + lth < 0 or path[j+lth-1] == 0 or j + lth - 1 < 0:  # 범위 내에 없거나, 이미 경사로 설치한곳일때 판별
                                flag = False
                                break
                            if field[i][j-1] != field[i][j+lth-1]:  # 만약 경사로 놓는 곳 범위 내에 높이가 다르면 못놓으므로
                                flag = False
                                break
                            else:
                                path[j+lth-1] = 0  # 방문표시
                            lth -= 1
                    if flag == True:
                        if L == 1:
                            j += 1
                        else:
                            j += 1
                            path[j] = 0
                    else:
                        break
        else:
            j += 1  # 다음칸으로 이동

    if flag == True:  # while문 잘 통과했다면 갈수있는길 - count 해준다
        cnt += 1

for j in range(N):  # 가로
    i = 1
    flag = True
    path = [1] * (N+1)  # 이미 경사로 놓은 자리 visit 표시해주는 리스트
    while True:
        if i >= N:
            break
        if field[i-1][j] != field[i][j]:  # 만약 경사로이면
            if abs(field[i-1][j] - field[i][j]) >= 2:  # 높이가 2 이상 차이나면 어차피 못하므로 Break
                flag = False
                break
            else:
                lth = 1
                if field[i-1][j] - field[i][j] > 0:  # 내리막길일때
                    while lth < L:
                        if i + lth >= N or path[i+lth] == 0:  # 범위 벗어나거나 이미 경사로 놓은거면
                            flag = False
                            break
                        if field[i][j] != field[i+lth][j]:  # 만약 경사로 놓는 곳 범위 내에 높이가 다르면 못놓으므로
                            flag = False
                            break
                        else:
                            path[i+lth-1] = 0  # 방문한데 표시
                        lth += 1
                    if flag == True:
                        if L == 1:  # 경사로 L = 1
                            i += 1
                        else:       # 상기와 마찬가지
                            i += lth
                            path[i-1] = 0
                    else:
                        break
                else:  # 오르막길
                    lth = -1
                    if L == 1:  # 경사로 L = 1 일떄
                        if i-2 >= 0 and field[i-2][j] == field[i][j]:  # 경사로 놓는데가 겹치는 구간인지 확인
                            flag = False
                    else:
                        while abs(lth) < L:
                            if i + lth < 0 or path[i+lth-1] == 0 or i + lth - 1 < 0:  # 범위 내에 없거나, 이미 경사로 설치한곳일때 판별
                                flag = False
                                break
                            if field[i-1][j] != field[i+lth-1][j]:  # 만약 경사로 놓는 곳 범위 내에 높이가 다르면 못놓으므로
                                flag = False
                                break
                            else:
                                path[i+lth-1] = 0  # 방문표시
                            lth -= 1

                    if flag:
                        if L == 1:
                            i += 1
                        else:
                            i += 1
                            path[i] = 0
                    else:
                        break
        else:
            i += 1  # 다음칸으로 이동

    if flag == True:  # while문 잘 통과했다면 갈수있는길 - count 해준다
        cnt += 1

print(cnt)