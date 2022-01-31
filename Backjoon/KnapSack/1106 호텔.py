# 배낭문제, 홍보 비용은 정수배 만큼 늘어 날 수 있다. ( 뒤에서 줄여나가는 방식 안됨 )

wanted_customer_count, n = map(int, input().split())

# 홍보 비용, 고객 수
advertisements = [ list(map(int, input().split())) for _ in range(n) ]

dp_client = [float('inf')] * ( wanted_customer_count + 101 )
dp_client[0] = 0

for cost, client in advertisements:

    for cli in range(client, len(dp_client)):
        dp_client[cli] = min(dp_client[cli - client] + cost, dp_client[cli])

print(min(dp_client[wanted_customer_count:]))