def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: (x[2], x[0], x[1]))
    is_connected = dict(zip(range(n), [False] * n))
    connected_islands = [costs[0][0], costs[0][1]]
    is_connected[costs[0][0]] = is_connected[costs[0][1]] = True

    answer += costs[0][2]

    while len(connected_islands) != n:
        for cost in costs:
            if is_connected[cost[0]] == True and is_connected[cost[1]] == False:
                connected_islands.append(cost[1])
                is_connected[cost[1]] = True
                answer += cost[2]
                break
            elif is_connected[cost[0]] == False and is_connected[cost[1]] == True:
                connected_islands.append(cost[0])
                is_connected[cost[0]] = True
                answer += cost[2]
                break

    return answer
