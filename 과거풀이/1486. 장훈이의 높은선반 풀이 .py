# 1486. 장훈이의 높은선반 풀이

T = int(input())
for Count in range(T):
    print("#{0} ".format(Count+1),end = '')
    N , B = map(int,input().split())
    List = list(map(int,input().split()))
    total = 0
    Answer = []
    def bubun(idx):
        global total
        if total >= B:
            Answer.append(total)
        if idx < N:
            total += List[idx]
            bubun(idx+1)
            total -= List[idx]
            bubun(idx+1)
    bubun(0)
    print(min(Answer) - B)