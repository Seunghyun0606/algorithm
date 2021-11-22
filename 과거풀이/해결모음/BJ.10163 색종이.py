# BOJ.10163 색종이 겹치기 문제
# 색종이가 다 덮혔을때의 면적을 구하는 것
# 색종이 N장이 주어졌을때, 맨 좌측 하단 좌표값, 과 가로 세로의 크기가 주어진다.
# 따라서 종이를 높을 맵을 0으로 다 통일한다음에 각 색종이마다 1 ~ 100 까지 번호를 부여한뒤,
# 해당하는 값을 count 해준다.

# 방법 2 // 뒤에서부터 놓으면서 놓자말자 count세고 만약 놓을 공간이 차있으면 안넣고 비어있으면 넣었을대 카운트한번 더함

import sys
sys.stdin = open('input.txt', 'r')


T = int(input())  # 색종이 장수

confetti = [ list(map(int, input().split())) for _ in range(T) ]  # 0, 1은 좌표 2, 3은 가로(열) 세로(행) 길이

put_map = [[0 for _ in range(101) ] for _ in range(101)]  # 0부터 시작 해서 101칸씩 100 x 100 좌표평면 만들어서 종이를 놓을거야
count_list = []

# map에 종이를 놓는 코드
for i in range(len(confetti)):
    for x in range(confetti[i][3]):  # 행이 움직일꺼야. 행은 세로 넓이랑 연관이있다.
        for y in range(confetti[i][2]):  # 열이 움직일꺼야. 열은 가로 넓이랑 연관있다.
            if confetti[i][1] + x < 101 and confetti[i][0] + y < 101:  # 놓는 인덱스가 맵 범위 100안에 들어가야해
                put_map[confetti[i][1] + x][confetti[i][0] + y] = i+1
            # (x, y) 좌표에서 x가 열과 관련있고, y가 행과 관련있다. 0 은 x값, 1은 y값이 들어있다.

for i in range(1, T+1):  # 색종이 장수만큼 값들이 들어갔을테니깐 그 각각의 값들을 탐색할거야. 첫번째 종이는 1의 값을 가진다.
    count = 0
    for x in range(len(put_map)):
        for y in range(len(put_map)):
            if put_map[x][y] == i:
                count += 1
    count_list += [count]

print(*count_list, sep='\n')