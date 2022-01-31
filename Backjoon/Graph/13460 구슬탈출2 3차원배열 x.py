# 빨간 구슬을 빼내고, 파란 구슬은 빠지면 안된다.
# 동시에 빠져도 실패다.
# 동시에 같은 칸에 있을 수 없다.
# 더 이상 구슬이 움직이지 않을 때 까지 기울인다.
# 빨간 구슬을 빼낼 최소 횟수
# string이므로, 숫자로 변환하면 메모리를 줄일순 있을거같네. 굳이 하진 말자.

# 3차원 배열을 사용하면 안된다.
# 3차원 배열을 이용할 경우, 둘 중 하나만 방문하지 않았을 경우 통과하게 해서 문제를 풀어야하는데,
# 이 경우, 4차원 배열에서 처럼 둘 모두가 방문하지 않았을 경우랑은 다른 경우의 수가 나오게 된다.
# 왜냐면, 갔던 지점에 또 갈 수도 있는데, 이 때, 방문 체크 여부가 달라지기 때문이다.
# 차라리 속도를 신경쓰지 않는다면, 방문체크를 하지 않는 것이 정답에 가깝다.

from collections import deque

n, m = map(int, input().split())

blue_place = []
red_place = []

board = []

for i in range(n):
    temp = input()
    for j in range(m):
        if temp[j] == "B":
            blue_place = [i, j]
        elif temp[j] == "R":
            red_place = [i, j]
    board.append(temp)

control = [ (0, 1), (1, 0), (-1, 0), (0, -1) ]

check_4 = [ [[0, 0] for _ in range(m)] for _ in range(n) ]

# 굴러간 거리가 더 먼 경우가 뒤에 있는 구슬.
# 즉, 더 멀리 굴러가면 해당 구슬은 한 칸 뒤로 빼주면 된다.
def move(_r, _c, _n, dr, dc):
    while not board[_r + dr][_c + dc] == "#" and not board[_r][_c] == "O":
        _r += dr
        _c += dc
        _n += 1
    return _r, _c, _n

def roll_game():

    que = deque( [red_place + blue_place + [0]] )
    while que:
        red_r, red_c, blue_r, blue_c, d = que.popleft()
        
        # 10번 이상 굴리면 안된다.
        if d > 10:
            continue

        for i in range(4):
            new_rr, new_rc, new_rn = move(red_r, red_c, 0, control[i][0], control[i][1])
            new_br, new_bc, new_bn = move(blue_r, blue_c, 0, control[i][0], control[i][1])

            # 파란색이 먼저들어가면 그 턴은 종료, 다시 시작
            if board[new_br][new_bc] == "O":
                continue
            if board[new_rr][new_rc] == "O":
                print(d + 1)
                return
            
            # 만약 구슬 위치가 같다면, 구슬이 굴러간 거리가 더 먼 구슬은 한칸 뒤로 뺀다
            if [ new_rr, new_rc ] == [ new_br, new_bc]:
                if new_rn > new_bn :
                    new_rr -= control[i][0]
                    new_rc -= control[i][1]
                else:
                    new_br -= control[i][0]
                    new_bc -= control[i][1]
            
            # que에 넣어준다
            if not check_4[new_rr][new_rc][0] or not check_4[new_br][new_bc][1] :
                check_4[new_rr][new_rc][0] = 1
                check_4[new_br][new_bc][1] = 1
                que.append([new_rr, new_rc, new_br, new_bc, d + 1])
    print(-1)

roll_game()

