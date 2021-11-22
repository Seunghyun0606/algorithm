# 문제2 희토류를 찾아라.
# 문제 background가 DFS를 써라했으니 DFS사용하자.


def find_rear_metal(x, y, metal):
    global count

    mount[x][y] = 0  # check를 위해서 0으로 만들어줌.
    count += 1
    for k in range(8):
        row = x + dx[k]
        col = y + dy[k]

        if n > row > -1 and n > col > -1:
            if mount[row][col] == metal:  # metal을 기준으로 넣어서 거기 있는 것만 계산
                find_rear_metal(row, col, metal)


T = int(input())

for tc in range(T):

    n = int(input())

    mount = [list(map(int, input().split())) for _ in range(n)]

    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    max_nums = 0
    min_count = 20*20
    for i in range(n):
        for j in range(n):
            if mount[i][j]:
                count = 0
                temp = mount[i][j]
                find_rear_metal(i, j, mount[i][j])

                if count*temp > max_nums:  # count*max가 최대 매장량
                    max_nums = count*temp
                    min_count = count
                elif count*temp == max_nums:  # 만약에 최대 매장량이 같을 시, 최소 면적을 뽑아내야한다.
                    min_count = min(count, min_count)



    print('#{}'.format(tc+1), max_nums, min_count)
