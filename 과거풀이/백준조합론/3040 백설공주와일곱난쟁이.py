n = 9
nums = [ int(input()) for _ in range(n) ]

check = [0]*n

def comb(k, num_sum, num_list):
    
    if k == 7 and num_sum == 100:
        print(*num_list, sep='\n')
        exit()  # exit 코드를사용하면 재귀함수를 바로 빠져나갈 수 있다.
    else:
        for i in range(k, n):
            if check[i]:
                continue
            check[i] = 1
            comb(k+1, num_sum + nums[i], num_list + [nums[i]])
            check[i] = 0
comb(0, 0, [])


# 생각의 전환, 9개의 수중에서 7개만 합쳐서 100이니깐 두개만 빼면 답이 나온다는 생각.
# o_o=[]
# sum=0
# for i in range(9):
#     n=int(input())
#     sum=sum+n
#     o_o.append(n)
# for k in o_o:
#     for j in o_o:
#         if k+j==sum-100 and k!=j:
#             o_o.remove(k)
#             o_o.remove(j)
# for l in o_o:
#     print(l)
