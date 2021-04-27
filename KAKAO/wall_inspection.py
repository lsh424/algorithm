from collections import defaultdict

def solution(n, weak, dist):
    dic = defaultdict(list)
    answer = 1
    dist.sort(reverse=True)

    for d in dist:
        for i in weak:
            s = set()
            for j in weak:
                if j - i >= 0:
                    term = j - i
                    if d >= term:
                        s.update({j, i})
                    else:
                        continue
                elif j - i < 0:
                    term = j - i + n
                    if d >= term:
                        s.update({j, i})
                    else:
                        continue
            if len(s) > 0:
                if s not in dic[d]:
                    dic[d].append(s)

    all = set()

    for i in dist:
        if all:
            ss = set()
            for j in dic[i]:
                for k in all:
                    s = set(k) | j
                    if len(s) == len(weak):
                        return answer
                    else:
                        ss.add(tuple(s))

            all = ss
        else:
            for j in dic[i]:
                if len(j) == len(weak):
                    return answer
                else:
                    all.add(tuple(j))

        answer += 1

    return -1