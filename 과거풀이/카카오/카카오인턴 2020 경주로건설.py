# 좌표, 자동차의 방향을 정해야한다.
# check 배열에는 자동차가 이동했을 때의 값을 저장한다
# 자동차의 방향이 같은 방향이었을 경우, 100, 다른 방향이었을 경우 600을 체크배열에 더해서 저장
# 왜냐면 어차피 다른방향으로 이동할때, 코너랑 직선도로가 같이 건설되기 때문.
# 만약에 저장된 값이 새로 넘어오는 값보다 작으면 갈 수 있다.

from collections import deque

def solution(board):
    dr = [1, 0, 0, -1]
    dc = [0, 1, -1, 0]
    # 하 우 좌 상 순서

    # answer = float('inf')

    where = deque()
    n = len(board)
    road_price = [ [ 0 for _ in range(n) ] for _ in range(n) ]
    for j in range(2):
    # where.append([0, 0, 0, 0])  # 아래방향을 바라보고 시작
        where.append([0, 0, j, 0])

        while where:
            # print()
            # print(*road_price, sep='\n')
            # print(where)
            x, y, d, p = where.popleft()

            for i in range(4):
                row = x + dr[i]
                col = y + dc[i]

                if n > row > -1 and n > col > -1 and not board[row][col]:
                    # price_a = road_price[x][y]    # 이동하기 전 큐에 저장된 현재 좌표
                    price = road_price[row][col]  # 이동하게 될 좌표
                    if i == d:
                        if price:
                            if p + 100 <= price:  # 새로 들어갈 값이 더 작으면 넣고, 큐에 넣어준다. 아니면 그냥 넘어간다.
                                road_price[row][col] = p + 100
                                where.append([row, col, i, road_price[row][col]])
                        else:  # price가 0이면 검증없이 그냥 넣는다.
                            road_price[row][col] = p + 100
                            where.append([row, col, i, road_price[row][col]])
                    else:
                        if price:
                            if p + 600 <= price:
                                road_price[row][col] = p + 600
                                where.append([row, col, i, road_price[row][col]])
                        else:
                            road_price[row][col] = p + 600
                            where.append([row, col, i, road_price[row][col]])
    # print(answer)
    # print(*road_price, sep='\n')
    answer = road_price[n-1][n-1]
    # print(answer)
    # print(*road_price)
    # print(answer)
    return answer

# a = 	[[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
# solution(a)