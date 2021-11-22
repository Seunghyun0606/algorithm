# if문의 길이가 짧아지니깐 속도도 빨라지더라. 근데 큰 차이는 아니긴함

chess = [ list(input()) for _ in range(8) ]
cnt = 0
for r in range(8):
    for c in range(8):
        if chess[r][c] == 'F' and ( r % 2 and c % 2 or not r%2 and not c%2 ):
                cnt += 1
print(cnt)