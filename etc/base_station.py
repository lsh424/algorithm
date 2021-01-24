def solution(n, stations, w):
    answer = 0
    pos = 1

    for station in stations:
        if station - w - pos > 0:
            if ((station - w - pos) / (1 + 2 * w)) > ((station - w - pos) // (1 + 2 * w)):
                answer += ((station - w - pos) // (2 * w + 1) + 1)

            else:
                answer += ((station - w - pos) // (2 * w + 1))

        pos = station + w + 1

    if stations[-1] + w < n:
        if (n - pos + 1) / (2 * w + 1) > (n - pos + 1) // (2 * w + 1):
            answer += ((n - pos + 1) // (2 * w + 1) + 1)
        else:
            answer += (n - pos + 1) // (2 * w + 1)

    return answer