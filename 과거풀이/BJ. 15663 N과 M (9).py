# 15663 N과 M (9)


def dfs(start, li1):
    if len(li1) == m:
        if li1 not in ept_li2:
            ept_li2.append()


        # ept_li2.append(li1)
    else:
        for i in range(1, n+1):
            if i == start:
                continue
            dfs(i, li1 + [li[i]])


n, m = map(int, input().split())

li = [0] + sorted(list(map(int, input().split())))
ept_li = []
ept_li2 = []
dfs(0, ept_li)

# ept_li2 += [0]
# for i in range(len(ept_li2)-1):
#     for j in range(i+1, len(ept_li2)):
#         if ept_li2[i] == ept_li2[j]:
#             break
#     else:
#         print(*ept_li2[i])


