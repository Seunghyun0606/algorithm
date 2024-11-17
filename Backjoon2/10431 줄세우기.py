# 자기 앞에 자기보다 키가 큰 학생이 없다면 그냥 그 자리에 서고 차례가 끝난다.
# 자기 앞에 자기보다 키가 큰 학생이 한 명 이상 있다면 그중 가장 앞에 있는 학생(A)의 바로 앞에 선다. 이때, A부터 그 뒤의 모든 학생들은 공간을 만들기 위해 한 발씩 뒤로 물러서게 된다.
# 걸음의 총 합을 구해야함
n = int(input())
tc = [ list(map(int, input().split())) for _ in range(n)]

for test in tc:
    mytc = test[1:]
    line = [mytc[0]]
    max_footage = 0
    for height_i in mytc[1:]:
        for idx, height in enumerate(line):
            if max(line) < height_i:
                line.append(height_i)
                break
            if height > height_i:
                calc_footage = len(line[idx:])
                line = line[:idx] + [height_i] + line[idx:]
                max_footage += calc_footage
                break
    print(test[0], max_footage)



# P=int(input())
# for _ in range(P):
#     arr=list(map(int,input().split()))
#     total=0
#     for i in range(1,len(arr)-1):
#         for j in range(i+1,len(arr)): # i 뒤에 애들과 전부 비교해서
#             if arr[i] > arr[j]:  # i가 더 크면
#                 arr[i],arr[j] = arr[j],arr[i]  # 자리바꾸기
#                 total+=1
#     print(arr[0], total)

# line = [1,2,3]

# print (line[:1] + [4] + line[1:])