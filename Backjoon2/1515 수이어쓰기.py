
# N까지의 숫자를 줄세워놓고, 해당숫자까지 갈때까지
# 주어진 nums들의 숫자가 다 나왔는지 확인해야한다.

nums = input()
n = 0
idx = 0
while True:
    n += 1

    for s in str(n):
        if nums[idx] == s:
            idx += 1
            if idx >= len(nums):
                print(n)
                exit()
