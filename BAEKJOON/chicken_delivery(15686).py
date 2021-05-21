#### 15686(치킨 배달)
import itertools

n, m = map(int, input().split(' '))
g = []
chickens = []
homes = []
answer = float('inf')

for i in range(n):
    ls = list(map(int, input().split(' ')))
    g.append(ls)
    for j in range(len(ls)):
        if ls[j] == 1:
            homes.append([i, j])
        elif ls[j] == 2:
            chickens.append([i, j])

chick_comb = list(itertools.combinations(chickens, m))

for chick in chick_comb:
    total_d = 0
    for h in homes:
        min_d = float('inf')
        for c in chick:
            d = abs(c[0] - h[0]) + abs(c[1] - h[1])
            min_d = min(min_d, d)
        total_d += min_d

    answer = min(answer, total_d)

print(answer)