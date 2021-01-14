def solution(routes):
    answer = 1

    routes.sort()
    boundary = routes[0]

    for route in routes:
        if route[0] >= boundary[0] and route[0] <= boundary[1]:
            if route[0] > boundary[0]:
                boundary[0] = route[0]

            if route[1] < boundary[1]:
                boundary[1] = route[1]
        else:
            answer += 1
            boundary[0] = route[0]
            boundary[1] = route[1]

    return answer