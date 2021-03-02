def solution(brown, yellow):
    yellow_list = []

    for i in range(1, yellow + 1):
        if yellow // i < i:
            break

        if yellow % i == 0:
            yellow_list.append([yellow // i, i])

    for t in yellow_list:
        if sum(t) == (brown - 4) / 2:
            return [t[0] + 2, t[1] + 2]