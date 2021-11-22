from collections import defaultdict

n = int(input())

cards_dict = defaultdict(int)

for card in list(map(int, input().split())):
    cards_dict[card] += 1

m = int(input())

for number in list(map(int, input().split())):
    print(cards_dict[number], end=' ')