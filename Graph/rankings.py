from collections import defaultdict

def solution(n, results):
    answer = 0
    wins = defaultdict(set)
    defeats = defaultdict(set)

    for (a, b) in results:
        wins[a].add(b)
        defeats[b].add(a)

    for i in range(1, n + 1):
        for winner in defeats[i]:
            wins[winner].update(wins[i])

        for loser in wins[i]:
            defeats[loser].update(defeats[i])

    for i in range(1, n + 1):
        if len(wins[i]) + len(defeats[i]) == n - 1:
            answer += 1

    return answer