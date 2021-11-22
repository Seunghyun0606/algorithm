N = int(input())

for n in range(N):
    h, w, m = map(int, input().split())

    prior, back = (str(m % h), str(m // h + 1)) if m%h else (str(h), str(m//h))
    print(prior + '0' + back) if len(back) == 1 else print(prior+back)