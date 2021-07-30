# 동굴에서 최소금액을 잃고 돌아가기. 상하좌우 1칸씩 이동 가능

import heapq, sys
input = sys.stdin.readline

T = 1
while True:

    n = int(input())

    if not n:
        break

    # 동굴 형성
    cave = [ list(map(int, input().split())) for _ in range(n) ]

    # dp를 위한 rupy 형성
    rupy = [ [float('inf')] * n for _ in range(n) ]
    rupy[0][0] = cave[0][0]

    # heap 형성
    heap = []
    heapq.heappush(heap, (cave[0][0], 0, 0))

    # 상하좌우 움직이기
    move_row = [1, -1, 0, 0]
    move_col = [0, 0, 1, -1]

    # 다익스트라 시작
    while heap:
        current_rupy, current_row, current_col = heapq.heappop(heap)

        if rupy[current_row][current_col] >= current_rupy:

            for i in range(4):
                row = current_row + move_row[i]
                col = current_col + move_col[i]

                if n > row > -1 and n > col > -1:
                    total_rupy = current_rupy + cave[row][col]

                    if rupy[row][col] > total_rupy:
                        rupy[row][col] = total_rupy
                        heapq.heappush(heap, (total_rupy, row, col))

    print(f'Problem {T}: {rupy[n-1][n-1]}' )

    T += 1
            


