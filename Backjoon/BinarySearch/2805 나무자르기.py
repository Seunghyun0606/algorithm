n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 절단기의 최대 높이를 구해야함 -> 이분 탐색 구간
# 최대 높이는 나무 최대 높이, 최소는 0
# 나무 합이 적어도 m ( 최소 m 이상 )
min_cut = 0
max_cut = max(trees)

target_h = 0
while max_cut >= min_cut :
    mid = ( max_cut + min_cut ) // 2

    cut_h = 0

    for tree in trees:
        cut_tree = tree - mid
        if cut_tree > 0:
            cut_h += cut_tree

    if cut_h >= m:
        min_cut = mid + 1
        target_h = max(target_h, mid)
    else:
        max_cut = mid - 1

print(target_h)