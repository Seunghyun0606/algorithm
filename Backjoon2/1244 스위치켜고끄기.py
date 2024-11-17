# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 
# 그 구간에 속한 스위치의 상태를 모두 바꾼다. 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.


_ = int(input())
switch_list = list(map(int, input().split()))
n = int(input())
play_game = [ list(map(int, input().split())) for _ in range(n) ]

for play in play_game:
    who, num = play
    
    if who == 1:
        cnt = 1
        while len(switch_list) >= num*cnt:
            if switch_list[num*cnt - 1]:
                switch_list[num*cnt - 1] = 0
            else:
                switch_list[num*cnt - 1] = 1
            cnt += 1
    else:
        # 양 끝단은 대칭적일 수 없다
        if num == 1 or num == len(switch_list):
            if switch_list[0]:
                switch_list[0] = 0
            else:
                switch_list[0] = 1
        else:
            i = 1
            # 자기 위치꺼는 무조건 바꿈
            if switch_list[num-1]:
                switch_list[num-1] = 0
            else:
                switch_list[num-1] = 1
            # 범위에 있는 애들 바꾸기
            while num - 1 + i < len(switch_list) and num - 1 - i >= 0:
                if switch_list[num - 1 + i] == switch_list[num - 1 - i]:
                    # print(switch_list[num-1+i])
                    if switch_list[num-1+i]:
                        switch_list[num-1+i] = 0
                        switch_list[num-1-i] = 0
                    else:
                        switch_list[num-1+i] = 1
                        switch_list[num-1-i] = 1
                    i += 1
                else:
                    break
rows = len(switch_list) // 20
if rows == 0 or len(switch_list) == 20:
    print(*switch_list)
else:
    j = 0
    for _ in range(rows):
        # print('=====', j)
        print(*switch_list[j:j+20])
        j += 20
    print(*switch_list[j:])

# 62
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 2
# 1 3
# 2 3
# ===

# 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 1 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 1 0 0 1 1 0
# 21
# 1 0 0 1 1 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 1
# 2
# 1 3
# 2 3

# 1 1 0 1 1 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 
# 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 
# 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0
        
#         입력:
# 8
# 0 1 0 1 0 0 0 1
# 5
# 1 3
# 2 3
# 2 5
# 1 6
# 1 7

# 출력:
# 1 0 0 0 0 1 0 1

# 정답:
# 1 0 0 0 0 0 1 1