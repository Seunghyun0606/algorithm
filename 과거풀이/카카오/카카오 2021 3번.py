# 시간초과;;;

def my_condition(condition):

    my_condition = filter(lambda x: x != 'and', condition.split())
    return  list(my_condition)

def check_condition(info, query):
    
    for i in range(4):
        if query[i] == '-' or query[i] == info[i]:
            continue
        else:
            return False
    # if info[4] >= query[4]:
    #     return True
    # else:
    #     False

    return True if int(info[4]) >= int(query[4]) else False

def solution(info, query):

    new_info = list(map(lambda  x: x.split(), info))  # 리스트형태로 만들어서 필터하기 쉽게만들자.

    new_query = list(map(my_condition, query))  # 리스트 형태로 만들어서 필터조건 넣기 쉽게 만들자.

    query_count = []
    for query in new_query:
        count = 0
        for info in new_info:
            if check_condition(info, query):
                count += 1
        query_count.append(count)

    # print(new_info)
    # print(new_query)
    # print(query_count)

    answer = query_count
    return answer

test = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
# a = "java and backend and junior and pizza 100"

a = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

solution(test, a)

# print(list(b))
# b = map(str, a.split())
# c = list(b)
# d = filter(lambda x: x != 'and', c)
# # print(c)

# # print(d)
# k = list(d)
# print(k)
# # print(*d)
# con1 = lambda x : x in test[0]
# con2 = lambda x : x in test[0]
# con3 = lambda x : x in test[0]
# con4 = lambda x : x in test[0]
# con5 = lambda x : x 

# con = [con1, con2, con3, con4, con5]

# e = all(map(lambda t: all(f(t) for f in con), k))

# print(e)