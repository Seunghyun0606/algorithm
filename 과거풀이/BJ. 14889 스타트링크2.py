# BJ. 14889 스타트링크


def team(depth, idx):
    global flag

    if flag:
        players[idx] = 1

        if depth == n // 2:
            a = 0
            b = 0
            # a팀 b팀 한번에 계산함. 1일때는 a팀 0일때는 B팀
            a_list = []
            b_list = []
            for i in range(1, n+1):
                if players[i]:
                    a_list += [i-1]
                else:
                    b_list += [i-1]

            for i in a_list:
                for j in a_list:
                    a += abilities[i][j]
            for i in b_list:
                for j in b_list:
                    b += abilities[i][j]

            global ability_min

            if a-b == 0:
                ability_min = 0
                flag = False
                return

            if ability_min > abs(a-b):
                ability_min = abs(a-b)

        else:
            for i in range(idx+1, n+1):
                if players[i]:
                    continue
                team(depth+1, i)
                players[i] = 0


n = int(input())

abilities = [ list(map(int, input().split())) for _ in range(n)]

players = [0] * (n+1)
flag = True
ability_min = 100 * 20

team(0, 0)

print(ability_min)




