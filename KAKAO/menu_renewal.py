from collections import defaultdict
import itertools

def solution(orders, course):
    dic = defaultdict(int)
    candidates = defaultdict(list)

    for order in orders:
        for c in course:
            if len(order) < c:
                break
            for j in itertools.combinations(sorted(order), c):
                dic[''.join(j)] += 1

    for k, v in dic.items():
        if v >= 2:
            if not candidates[len(k)]:
                candidates[len(k)].append((k, v))
            else:
                if candidates[len(k)][-1][1] == v:
                    candidates[len(k)].append((k, v))
                elif candidates[len(k)][-1][1] < v:
                    candidates[len(k)] = [(k, v)]

    return sorted([v[0] for ls in candidates.values() for v in ls])

################
# Counter 사용하면 조금 더 간단하게 풀림
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]