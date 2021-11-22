# 6109. 추억의 2048게임 D4

# 한방향으로의 해결법을 만든다음에 좌표를 바꾸는 방법을 사용할 것이다.

def my_rotate(matrix, rot):
    n1 = len(matrix)
    new_matrix = [[ 0 for _ in range(n1) ] for _ in range(n1)]
    if rot == 'up':
        return matrix
    elif rot == 'left':
        for col in range(n1):
            for row in range(n1):
                new_matrix[row][n1 - col - 1] = matrix[col][row]  # 90도 회전시, 행을 고정시키던걸 열을 고정시키고 행을 움직이게됨
        return new_matrix
    elif rot == 'right':  # 사실상 90도 회전 3번 for문 돌리면됨
        for col in range(n1):
            for row in range(n1):
                new_matrix[n1 - row - 1][col] = matrix[col][row]
        return new_matrix
    elif rot == 'down':
        for col in range(n1):
            for row in range(n1):
                new_matrix[n1 - col - 1][row] = matrix[col][row]
        return new_matrix


import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):

    n, direct = input().split()
    n = int(n)

    default_map = [list(map(int, input().split())) for _ in range(n)]

# 좌표 받은후, direct 가 up, down, left, right 에 따라 좌표 위치를 바꿔줄예정
# up은 그대로, down은 아래위만 바꾼다. left는 시계 90, right는 반시계 90 바꾼다음 다시원위치

    game_map = my_rotate(default_map, direct)  # 회전시켜주었다.

    flag = True
    flag_2 = True
    present_p = 0

    # up일때의 경우, 해결하는 방법.
    for y in range(n):  # up의 경우 열을 옮겨나간다.
        count = -1
        count_0 = 0  # count 0의 갯수를 구해서 밑에서 0을 밀어올릴때 써먹는다
        while flag:
            if count == n - 1:  # 마지막값은 비교할필요없으니깐.
                break
            x = 0
            count += 1  # 0번 인덱스에서 시작했다. 모든인덱스를 같은작업하려면 count = 4 // n-1번 즉 이게 행방향을 바꿔주는 거고
            present_p = game_map[x + count][y]  # 현재 내가 비교하고 싶은 값을 넣어준것

            while flag_2:  # 여기는 지정 행 위치에서 그 밑에 행들을 비교해나가는거
                if present_p == 0:  # 시작 값이 0이면 그냥 넘어감
                    count_0 += 1
                    break
                x += 1
                if x + count == n:
                    break
                if game_map[x + count][y] == 0:  # 다음 값이 0이면 그냥 넘어가
                    count_0 += 1
                    continue
                if present_p == game_map[x + count][y]:  # 만약 같은 값을 만나면 곱하고 바꿔
                    # present_p *= 2
                    game_map[count][y] *= 2
                    game_map[x + count][y] = 0
                    count_0 += 1
                    break  # 만약바꿨으면 내가 기준으로 잡은 값은 더이상 비교안해도된다.
                if present_p != game_map[x + count][y]:  # 만약 다른 값을 만나면 행방향 검색 그만하고 다음 행로 넘어가
                    break
        # 다 더해줬으니 여기서부터 0인부분 찾고 올리자
        for _ in range(count_0):
            x = -1
            while x < n-2: # n = 5일때 인덱스가 4까지다. x+1을 쓸거기 때문에 x는 3을넘으면 안된다.
                x += 1
                if game_map[x][y] == 0:  # 0갯수만큼 반복한다.
                    game_map[x][y] = game_map[x+1][y]
                    game_map[x+1][y] = 0  # 0을만나면 밑에있는걸 위로 올리고, 그자리를 0으로만듬

    # 다 끝나고 다시 재회전 시켜준다.
    if direct == 'right':
        game_map = my_rotate(game_map, 'left')
    elif direct == 'left':
        game_map = my_rotate(game_map, 'right')
    else:
        game_map = my_rotate(game_map, direct)


    print('#{}'.format(tc + 1))
    for game in game_map:
        print(*game)

