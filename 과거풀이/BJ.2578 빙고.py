
my_bingo1 = [ list(map(int, input().split())) for _ in range(5)]

try_bingo1 = []
for _ in range(5):
    try_bingo1 += list(map(int, input().split()))  # 2차원만들지말고 하나로 받아와

def plz_bingo(my_bingo, try_bingo):

    count = 0
    for i in try_bingo:
        for y in range(5):
            for x in range(5):  # bingo판 크기
                if my_bingo[x][y] == i:
                    my_bingo[x][y] = -1
                    count += 1
                flag = True
                while flag and count > 11:
                    bingo = 0
                    for y1 in range(5):
                        bingo_find = 0
                        for x1 in range(5):  # 행탐색해서 빙고있는지 알아본다.
                            if my_bingo[x1][y1] == -1:
                                bingo_find += 1
                        if bingo_find == 5:
                            bingo += 1
                            if bingo == 3:
                                return count

                    for x2 in range(5):
                        bingo_find = 0
                        for y2 in range(5):  # 열탐색해서 빙고잇는지 알아본다.
                            if my_bingo[x2][y2] == -1:
                                bingo_find += 1
                        if bingo_find == 5:
                            bingo += 1
                            if bingo == 3:
                                return count

                    bingo_find = 0
                    for dia1 in range(5):
                        if my_bingo[dia1][dia1] == -1:
                            bingo_find += 1
                    if bingo_find == 5:
                        bingo += 1
                        if bingo == 3:
                            return count

                    bingo_find = 0
                    for dia2 in range(5):
                        if my_bingo[5-dia2-1][dia2] == -1:
                            bingo_find += 1
                    if bingo_find == 5:
                        bingo += 1
                        if bingo == 3:
                            return count
                    flag = False

print(plz_bingo(my_bingo1, try_bingo1))