n = int(input())

nList = list(map(int, input().split()))

m = int(input())
mList = list(map(int, input().split()))

nList.sort()

for target in mList:
    left = 0
    right = n - 1
    
    while right >= left:
        mid = ( left + right ) // 2

        if nList[mid] > target:
            right = mid - 1
        elif nList[mid] < target:
            left = mid + 1
        else:
            print(1)
            break
    else:
        print(0)
    
    

