# 빨간 구슬을 빼내고, 파란 구슬은 빠지면 안된다.
# 동시에 빠져도 실패다.
# 동시에 같은 칸에 있을 수 없다.
# 더 이상 구슬이 움직이지 않을 때 까지 기울인다.
# 빨간 구슬을 빼낼 최소 횟수
# string이므로, 숫자로 변환하면 메모리를 줄일순 있을거같네. 굳이 하진 말자.

# 4차원 배열을 사용하여 Check해줘야하나 보다.



from collections import deque

n, m = map(int, input().split())

# 기본 세팅
game_map = []

red = []
blue = []
min_move_count = 11

row = [0, 0, 1, -1]
col = [1, -1, 0, 0]

for i in range(n):
    temp_row = list(input())
    for j in range(m):
        if temp_row[j] == "R":
            red += [i, j, 0]
        elif temp_row[j] == "B":
            blue += [i, j, 0]
    game_map.append(temp_row)

# 큐에 빨강 블루 두개를 동시에 넣고, 두개씩 빼서 판단. 좌표, count 만약에 못움직이더라도, 못움직인데로 큐에 넣는다.
# 같은 위치에서 반복할 수도 있으니, 큐에 넣은 움직인 횟수 count 10회를 넘어가면 종료

move_place = deque()

move_place.append(red)
move_place.append(blue)


# 벽에 닿을때까지 굴러가야한다.
# 벽이나 다른 구슬에 닿으면, 그 이전자리로 돌아간다.
def move_ball(color_count, opper_color, cor_row, cor_col, k):
    global min_move_count

    while True:
        cor_row = cor_row + row[k]
        cor_col = cor_col + col[k]

        if game_map[cor_row][cor_col] == "#" or game_map[cor_row][cor_col] == opper_color:
            move_place.append([cor_row - row[k], cor_col - col[k], color_count + 1])
            return False
        elif game_map[cor_row][cor_col] == "O":
            if opper_color == "R":
                return True
            else:
                return color_count + 1

flag = True
while move_place:
    red_r, red_c, red_count = move_place.popleft()
    blue_r, blue_c, blue_count = move_place.popleft()

    # count가 10회가 넘어가면 그 que는 버린다
    if red_count > 10:
        continue

    start_color = "R"
    for i in range(4):
        red_row = red_r
        red_col = red_c

        # 빨간구슬과 파란구슬중 뭐가 먼저 굴러가야하지 정해야한다.
        while True:
            red_row = red_row + row[i]
            red_col = red_col + col[i]

            if game_map[red_row][red_col] == "B":
                start_color = "B"
                break
            elif game_map[red_row][red_col] == "#":
                break
        
        # 구슬을 굴린다.
        if start_color == "R":
            # 빨간색이 시작이고, 먼저들어가더라도, 파란색이 들어가면 실패.
            hole_in = False
            temp_min_count = move_ball(red_count, "B", red_r, red_c, i)
            hole_in = move_ball(blue_count, "R", blue_r, blue_c, i)

            # 들어가면 실패, 다시 시작
            if hole_in:
                # 블루는 들어갔는데, 빨강은 안들어가면 red stack 빼줘야함
                if temp_min_count:
                    move_place.pop()
                continue
            # 벽에 안부딪히고, 블루가 안들어갔으면, 들어간거 블루 스택 하나 빼주고, min 활성화 
            if temp_min_count:
                move_place.pop()
                min_move_count = min(min_move_count, temp_min_count)

        else:
            # 파란색이 시작이고, 먼저들어가면, 빨간색은 더이상 할 필요 없다.
            if move_ball(blue_count, "R", blue_r, blue_c, i):
                continue
            move_ball(red_count, "B", red_r, red_c, i)

print(min_move_count if min_move_count < 11 else -1)