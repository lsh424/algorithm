import collections

def solution(genres, plays):
    answer = []
    dic = collections.defaultdict(list)

    for i in range(len(genres)):
        if not dic[genres[i]]:
            dic[genres[i]].append(0)
            dic[genres[i]].append((i,plays[i]))
        else:
            dic[genres[i]].append((i,plays[i]))

        dic[genres[i]][0] += plays[i]

    ls = sorted(dic.items(), key = lambda x: x[1][0], reverse = True)

    for i in ls:
        t = sorted(i[1][1:], key = lambda x: (x[1], -x[0]), reverse = True)
        answer.append(t[0][0])
        try:
            answer.append(t[1][0])
        except:
            pass

    return answer