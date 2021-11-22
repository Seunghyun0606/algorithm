const_cost, variable_cost, sales = map(int, input().split())

if variable_cost >= sales:
    print(-1)
else:
    answer = (const_cost // (sales-variable_cost)) + 1
    print(answer)
