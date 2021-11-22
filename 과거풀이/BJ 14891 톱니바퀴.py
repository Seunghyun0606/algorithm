# BJ 14891 톱니바퀴  비트연산자쓰면 개빨리풀수있을거같은데. 가중치도 0, 1, 2, 3 이잖아 비트연산자로
# 2번 3시방향, 6번 9시방향. 0번 12시방향
# 1, 2, 4, 8 12시방향 가중치
# N극은 0, S극은 1


def rotation(idx, clock):
    if clock > 0:
        a = gears[idx].pop()
        gears[idx] = [a] + gears[idx]

    else:
        a = gears[idx][0]
        del gears[idx][0]
        gears[idx] += [a]


gears = [0] + [ list(map(int, list(input()))) for _ in range(4) ]

r = int(input())
rotate = [ list(map(int, input().split())) for _ in range(r)]
# 1 시계, -1 반시계
# 시계로돌면 pop해서 맨앞에 넣고
# 반시계로돌면 맨앞에껄 빼서 맨뒤로 넣는다.


for i in range(r):
    if rotate[i][0] == 1:
        if gears[1][2] != gears[2][6]:
            if gears[2][2] != gears[3][6]:
                if gears[3][2] != gears[4][6]:
                    rotation(1, rotate[i][1])
                    rotation(2, -rotate[i][1])
                    rotation(3, rotate[i][1])
                    rotation(4, -rotate[i][1])
                    continue
                rotation(1, rotate[i][1])
                rotation(2, -rotate[i][1])
                rotation(3, rotate[i][1])
                continue
            rotation(1, rotate[i][1])
            rotation(2, -rotate[i][1])
            continue
        elif gears[1][2] == gears[2][6]:
            rotation(1, rotate[i][1])
            continue

    elif rotate[i][0] == 4:
        if gears[4][6] != gears[3][2]:
            if gears[3][6] != gears[2][2]:
                if gears[2][6] != gears[1][2]:
                    rotation(4, rotate[i][1])
                    rotation(3, -rotate[i][1])
                    rotation(2, rotate[i][1])
                    rotation(1, -rotate[i][1])
                    continue
                rotation(4, rotate[i][1])
                rotation(3, -rotate[i][1])
                rotation(2, rotate[i][1])
                continue
            rotation(4, rotate[i][1])
            rotation(3, -rotate[i][1])
            continue
        elif gears[4][6] == gears[3][2]:
            rotation(4, rotate[i][1])
            continue

    elif rotate[i][0] == 3:
        if gears[3][2] != gears[4][6]:  # 오른쪽이 다를때, 왼쪽여부
            if gears[3][6] != gears[2][2]:  # 왼쪽
                if gears[2][6] != gears[1][2]:
                    rotation(3, rotate[i][1])
                    rotation(4, -rotate[i][1])
                    rotation(2, -rotate[i][1])
                    rotation(1, rotate[i][1])
                    continue
                rotation(3, rotate[i][1])
                rotation(4, -rotate[i][1])
                rotation(2, -rotate[i][1])
                continue
            rotation(3, rotate[i][1])
            rotation(4, -rotate[i][1])
            continue
        elif gears[3][2] == gears[4][6]: # 오른쪽은 같을때, 왼쪽여부
            if gears[3][6] != gears[2][2]: # 왼쪽
                if gears[2][6] != gears[1][2]:
                    rotation(3, rotate[i][1])
                    rotation(2, -rotate[i][1])
                    rotation(1, rotate[i][1])
                    continue
                rotation(3, rotate[i][1])
                rotation(2, -rotate[i][1])
                continue
            rotation(3, rotate[i][1])
            continue

    else:
        if gears[2][6] != gears[1][2]:  # 왼쪽이 다를때, 오른쪽여부
            if gears[2][2] != gears[3][6]:
                if gears[3][2] != gears[4][6]:
                    rotation(2, rotate[i][1])
                    rotation(1, -rotate[i][1])
                    rotation(3, -rotate[i][1])
                    rotation(4, rotate[i][1])
                    continue
                rotation(2, rotate[i][1])
                rotation(1, -rotate[i][1])
                rotation(3, -rotate[i][1])
                continue
            rotation(2, rotate[i][1])
            rotation(1, -rotate[i][1])
            continue
        elif gears[2][6] == gears[1][2]:  # 왼쪽이 같을때, 오른쪽여부
            if gears[2][2] != gears[3][6]:
                if gears[3][2] != gears[4][6]:
                    rotation(2, rotate[i][1])
                    rotation(3, -rotate[i][1])
                    rotation(4, rotate[i][1])
                    continue
                rotation(2, rotate[i][1])
                rotation(3, -rotate[i][1])
                continue
            rotation(2, rotate[i][1])
            continue

result = gears[1][0] + gears[2][0]*2 + gears[3][0]*4 + gears[4][0]*8

print(result)


