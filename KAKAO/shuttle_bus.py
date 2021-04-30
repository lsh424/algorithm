import collections

def solution(n, t, m, timetable):
    timetable = collections.deque(sorted([int(time[:2]) * 60 + int(time[3:]) for time in timetable]))
    bus_time = 540
    answer = 0
    c = 0

    for i in range(n):
        bus_time = 540 + (i * t)
        remain = m
        while remain:
            if timetable and timetable[0] <= bus_time:
                p = timetable.popleft()
                remain -= 1
                if c < p:
                    c = p
            else:
                answer = bus_time
                break

    if remain > 0:
        answer = bus_time
    else:
        answer = min(c, bus_time) - 1

    h, m = divmod(answer, 60)
    return str(h).zfill(2) + ':' + str(m).zfill(2)