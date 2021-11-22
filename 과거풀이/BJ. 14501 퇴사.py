# BJ. 14501 퇴사


def work_max(days, profits):
    if days == n:
        if profits > profits_max[0]:
            profits_max[0] = profits
    elif days > n:
        return

    else:
        for i in range(days, n):
            work_max(i + works[i][0], profits + works[i][1])

            if profits > profits_max[0]:
                profits_max[0] = profits


n = int(input())
works = [ list(map(int, input().split())) for _ in range(n)]

profits_max = [0]

work_max(0, 0)
print(*profits_max)

