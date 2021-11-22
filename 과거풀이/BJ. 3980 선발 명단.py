# BJ. 3980 선발 명단


def line_up(player, best):

    if player == 11:
        global power_max
        if best > power_max:
            power_max = best
    else:
        for j in range(11):
            if ability[player][j]:
                if position[j]:
                    continue
                position[j] = 1
                line_up(player+1, best + ability[player][j])
                position[j] = 0

T = int(input())

for _ in range(T):

    ability = [list(map(int, input().split())) for _ in range(11)]

    power_max = 0
    position = [0] * 11

    line_up(0, 0)

    print(power_max)

