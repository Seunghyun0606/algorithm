# def solve(kg):

#     real_answer = kg
#     n = 0  # 5일때
#     while True:
#         m = 0
#         answer = 0
#         answer += 5*n
#         if answer > kg:
#             break
#         elif answer == kg:
#             real_answer = min(real_answer, n)
#             break

#         while True:
#             answer += 3
#             m += 1
#             if answer > kg:
#                 break
#             elif answer == kg:
#                 real_answer = min(real_answer, n + m)
#                 break

#         n += 1
#     if real_answer == kg:
#         print(-1)
#     else:
#         print(real_answer)

# solve(int(input()))

# bongji = int(input())


# def sugar() :
#     for x in range((bongji // 3) + 1) : 
#         for y in range((bongji // 5) + 1) :
#             if(3 * x + 5 * y == bongji) :
#                 return x + y

    
#     return -1
# print(sugar())


# ???
n=int(input())
print(-(n in [4, 7]) or n-2*n//5*2)