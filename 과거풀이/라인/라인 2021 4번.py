# 미로 왼손법칙, 방향을 나타내는게 있어야함.
# 방향의 왼쪽에 벽에있는지 확인하고, 있으면 앞으로, 없으면 왼쪽으로 돌아서 앞으로이동한다.
# DFS로 풀어야한다.



def solution(maze):
    answer = 0

    # 현재 바라보는 방향, 0 1 2 3 (아래, 오른쪽, 위, 왼쪽)
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    # 좌측 방향 탐색
    lr = [0, -1, 0, 1]
    lc = [1, 0, -1, 0]

    n = len(maze)

    for i in range(n):
        maze[i] = [1] + maze[i] + [1]

    new_maze = [[1]*(n+2)] + maze + [[1]*(n+2)]
    visit = [ [0 for _ in range(n+2)] for _ in range(n+2) ]
    
    count = 0
    count_set = []

    def dfs(vx, vy, i):
        nonlocal count


        visit[vx][vy] = 1
        new_maze[vx][vy] = 1

        if vx == n-2 and vy == n-2:
            return
        else:
            flag = True
            cnt = 0
            while flag and cnt < 4:
                if i == 4:
                    i = 0
                row = vx + dr[i]
                col = vy + dc[i]
                l_row = vx + lr[i]
                l_col = vy + lc[i]
                if n > row > -1 and n > col > -1:
                    if visit[row][col]:
                        i += 1
                        cnt += 1
                        continue
                    if new_maze[l_row][l_col] and not new_maze[row][col]:  # 나아갈 방향 왼쪽에 벽이있으면서 전진 방향에 벽이없으면 전진
                        count += 1
                        dfs(row, col, i)
                        # flag = False
                    elif not new_maze[l_row][l_col]:
                        count += 1
                        dfs(l_row, l_col, i+1)   # 왼쪽에 벽이없으면 왼쪽으로 이동.
                        # flag = False
                i += 1
                cnt += 1

    dfs(1, 1, 0)  # 아래 오른쪽
    # count_set.append(count)
    # count = 0

    # dfs(1, 1, 1)  # 아래 오른쪽
    print(*visit, sep='\n')
    print(0)
    print(*new_maze, sep='\n')
    print(count)

            
    return answer

solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]])