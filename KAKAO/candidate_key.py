import itertools

def solution(relation):
    answer = 0
    ls = []
    select = 2
    candidates = []

    for c in range(len(relation[0])):
        s = set()
        for r in range(len(relation)):
            s.add(relation[r][c])
        if len(s) == len(relation):
            answer += 1
        else:
            ls.append(c)

    while select <= len(ls):
        columns = list(itertools.combinations(ls,select))
        remove_cand = set()
        for i in columns:
            s = set()
            for j in range(len(relation)):
                l = []
                for k in range(len(i)):
                    l.append(relation[j][i[k]])
                s.add(tuple(l))
            if len(s) == len(relation):
                for z in candidates:
                    if len(set(z) & set(i)) == len(z):
                        break
                else:
                    answer += 1
                    candidates.append(i)
        select += 1

    return answer

