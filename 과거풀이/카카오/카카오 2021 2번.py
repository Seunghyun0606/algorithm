

        
def solution(orders, course):

    def comb(k, bin, menus):

        if k == len(bin):
            comb_menus.append(tuple(bin))
            return
        else:
            for i in range(len(menus)):
                if check[i]:
                    continue
                check[i] = 1
                comb(k, bin + [menus[i]], menus)
                check[i] = 0


    answer = []

    menus = {}
    for i in orders:
        for j in i:
            menus[j] = 0

    menus = list(menus.keys())
    check = [0]*len(menus)


    make_menu = []

    for i in course:
        max_count = 0
        max_menu = []
        comb_menus = []
        comb(i, [], menus)
        comb_menus = set(comb_menus)
        for comb_menu in comb_menus:  # 2개면 [A, B] 두개를 order에서 검사
            count = 0
            for order in orders:    
                for menu in comb_menu: # A, B꺼냄
                    if menu in order:
                        continue
                    else:
                        break
                else:
                    count += 1
            if count > max_count:
                max_menu = []
                max_count = count
                temp = ''
                for menu in comb_menu:
                    temp += menu
                max_menu.append(temp)
            # elif count == max_count:
            #     temp = ''
            #     for menu in comb_menu:
            #         temp += menu
            #     max_menu.append(temp)

        for max_me in max_menu:
            make_menu.append(max_me)



    # orders = sorted(orders, key = lambda x : len(x))  # 순서대로 정렬
    # print(make_menu)

    return make_menu

# a = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# b = [2,3,4]

# solution(a, b)
