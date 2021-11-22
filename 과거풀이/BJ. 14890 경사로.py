# BJ. 14890 경사로
# for for 두개돌리고 else 로 break 안뜨면 count 하도록 만들자.
# 경사로 위로 갈때랑 아래로 갈때 두가지 케이스 만들어야함.


n, L = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(n)]
count = 0

# 가로로 하나씩 세어보자.
for i in range(n):
    temp = 1
    j = 0
    flag = False
    while j < n-1:
        if roads[i][j] == roads[i][j+1]:  # 같으면
            temp += 1
        elif roads[i][j] == roads[i][j+1] - 1:  # 올라가는거면
            if temp >= L:
                temp = 1
            else:
                break
        elif roads[i][j] == roads[i][j+1] + 1:  # 내려가는거면

            if j+L >= n:  # L개 채우기전에 끝에 닿으면 끝내.
                break
            for u in range(j+1, j+L):  # j + L + 1 까지 가능하지만 앞에꺼랑 비교하려고 -1 해준것
                if roads[i][u] != roads[i][u+1]:
                    flag = True
                    break
            if flag:
                break
            j = j+L  # 여기서부터 시작해야 그 다음에 올라가는지 안올라가는지도 알 수 있기 때문.
            temp = 0
            continue
        else:  # 경사로 높이 차이가 1 이상이면
            break
        j += 1
    else:
        count += 1

# 같은 작업을 세로에서 하는 것.
    temp = 1
    j = 0
    flag = False
    while j < n-1:  # 행 검사.
        if roads[j][i] == roads[j+1][i]:  # 같으면
            temp += 1
        elif roads[j][i] == roads[j+1][i] - 1:  # 올라가는거면
            if temp >= L:
                temp = 1
            else:
                break
        elif roads[j][i] == roads[j+1][i] + 1:  # 내려가는거면
            if j + L >= n:  # L개 채우기전에 끝에 닿으면 끝내.
                break
            for u in range(j + 1, j + L):
                if roads[u][i] != roads[u+1][i]:
                    flag = True
                    break
            if flag:
                break
            j = j + L
            temp = 0
            continue
        else:  # 경사로 높이 차이가 1 이상이면
            break
        j += 1
    else:
        count += 1

print(count)








