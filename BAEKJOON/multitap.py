import collections

n, k = map(int, input().split())
ls = list(map(int, input().split()))

answer = 0
current_s = set()
current_s.update(ls[:n])
capa = n - len(current_s)

remains = collections.deque(ls[n:])

while remains:
    if remains[0] in current_s:
        remains.popleft()
    elif capa > 0:
        current_s.add(remains.popleft())
        capa -= 1
    else:
        s = current_s.copy()
        for r in remains:
            s -= {r}
            if len(s) == 1:
                current_s -= s
                answer += 1
                current_s.add(remains.popleft())
                break

        if len(s) > 1:
            current_s.remove(s.pop())
            current_s.add(remains.popleft())
            answer += 1

print(answer)