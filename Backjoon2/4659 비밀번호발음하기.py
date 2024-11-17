# 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
# 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
# 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.


def check_rule2(um, three_word):
    cnt = 0
    for w in three_word:
        if w in um:
            cnt +=1
    return 1 if cnt ==3 else 0

while True:
    password = input()
    if password == 'end':
        break
    moum = set('aeiou')
    jaum = set('abcdefghijklmnopqrstuvwxyz') - moum
    rule1 = 0
    rule2 = 1
    rule3 = 1
    # 규칙1
    for m in moum:
        if m in password:
            rule1 = 1
            break
    # 규칙2
    if len(password) > 2:
        for i in range(len(password)-2):
            check_three_word = password[i:i+3]
            # print(check_three_word)
            
            r2_ja = check_rule2(jaum, check_three_word)
            r2_mo = check_rule2(moum, check_three_word)
            # print(r2_ja, r2_mo)
            if r2_ja + r2_mo > 0:
                rule2 = 0
                break
    
    # 규칙3
    if len(password) > 1:
        for i in range(len(password)-1):
            check_two_word = password[i:i+2]
            # print(check_two_word)
            if len(set(check_two_word)) == 1 and check_two_word[0] not in 'eo':
                rule3 = 0
                break
    # print(rule1, rule2, rule3)
    if ( rule1*rule2*rule3 ):
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')

            


    