def solution(brown, red):
    answer = []
    red_list = []

    for i in range(1, red + 1):
        if red % i == 0:
            ls = []
            ls.append(i)
            ls.append(red // i)
            red_list.append(ls)
            if i > red / i:
                break

    for ls in red_list:
        if sum(ls) + 4 == (brown + 4) / 2:
            ls.reverse()
            answer.append(ls[0] + 2)
            answer.append(ls[1] + 2)
            break

    return answer