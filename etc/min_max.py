def solution(s):
    ls = list(map(int, s.split(' ')))
    max_num = int(ls[0])
    min_num = int(ls[0])

    for i in ls:
        if i > max_num:
            max_num = i

        if i < min_num:
            min_num = i

    return str(min_num) + " " + str(max_num)