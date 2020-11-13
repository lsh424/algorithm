def solution(N, number):
    memo = []

    for i in range(1, 9):
        temp = {int(str(N) * i)}

        for j in range(0, i - 1):
            for m1 in memo[j]:
                for m2 in memo[-j - 1]:
                    temp.add(m1 + m2)
                    temp.add(m1 - m2)
                    temp.add(m1 * m2)

                    if m2 != 0:
                        temp.add(m1 // m2)

        if number in temp:
            return i

        memo.append(temp)

    return -1