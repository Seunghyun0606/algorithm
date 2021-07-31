# 바이러스가 퍼지지 못하도록 벽을 3개 세워서 최대 안전영역을 확보. BFS
# 벽을 먼저 3개 세우고 나서 찾는 것. 즉 벽 3개의 조합
# 최대 안전영역을 구하는 BFS 는 필요 없다.
# 전체 크기에서 벽갯수 빼고, 바이러스 퍼진 갯수 빼면 안전영역.

from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lab = []

lab_size = n*m
wall_count = 3
virus_place = []
space_list = []

# 바이러스 퍼지기위한 좌표
r = [1, -1, 0, 0]
c = [0, 0, 1, -1]

for i in range(n):
    temp = []
    for j_index, j in enumerate(map(int, input().split())):
        temp.append(j)
        if not j:
            space_list.append((i, j_index))
        elif j == 1:
            wall_count +=1
        else:
            virus_place.append((i, j_index))

    lab.append(temp)

# 최대 안전영역
max_safty = 0


# 방화벽을 통한 최대 안전영역
def find_safty_place(safty_wall_list):
    global max_safty

    mozo_lab = [ [ lab[i][j] for j in range(m) ] for i in range(n) ]


    # virus 갯수
    virus_count = len(virus_place)

    # 현재 안전 영억 크기
    current_safty = lab_size - virus_count - wall_count

    # 방화벽 설치
    for k in safty_wall_list:
        i, j = k
        mozo_lab[i][j] = 1


    # 바이러스 퍼뜨리기
    virus = deque(virus_place)
    
    while virus:
        vi_r, vi_c = virus.popleft()

        for i in range(4):
            row = vi_r + r[i]
            col = vi_c + c[i]

            if n > row > -1 and m > col > -1 and not mozo_lab[row][col]:
                virus.append((row, col))
                mozo_lab[row][col] = 2
                current_safty -= 1
                if current_safty <= max_safty:
                    return
    
    # 다 퍼지고 난 뒤 안전영역 크기
    max_safty = current_safty
    

# 방화벽 3개 조합
for space_comb in combinations(space_list, 3):
    find_safty_place(space_comb)

print(max_safty)