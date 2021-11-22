# BJ. 1309 동물원 (DP)
# 2 * n 의 우리가 있다. 가로 세로로는 배치 못한다.
# 사자는 최대 n개 있다.
# 1 ~ n 까지 마릿수를 꺼낸다.
# 0인경우 1 더해준다.
# dp로 3가지 경우를 나눈다. 현재 줄의 없는가? 있으면 왼쪽? 오른쪽?

n = int(input())

dp_no = [0]*(n+1)
dp_left = [0]*(n+1)
dp_right = [0]*(n+1)
dp_no[0] = 1
# 그냥 2차원으로 풀어도된다. 다만 1차원이 메모리랑 시간이 더 작게 먹는다.
# 0 이면 현재 줄에 없는 상태. 윗줄에 없거나 좌, 우 가능.

for i in range(1, n+1):
    dp_no[i] = (dp_no[i-1] + dp_left[i-1] + dp_right[i-1]) % 9901
    dp_right[i] = (dp_no[i-1] + dp_left[i-1]) % 9901
    dp_left[i] = (dp_no[i-1] + dp_right[i-1]) % 9901  # 이게없으면 오버플로우가 난다.

print((dp_no[n] + dp_left[n] + dp_right[n]) % 9901)