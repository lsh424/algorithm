import collections

def solution(bridge_length, weight, truck_weights):
    time = 0
    que = collections.deque([0] * bridge_length)
    truck_weights = collections.deque(truck_weights)

    while que:
        time += 1
        weight += que.popleft()

        if truck_weights:
            if weight >= truck_weights[0]:
                truck_weight = truck_weights.popleft()
                que.append(truck_weight)
                weight -= truck_weight
            else:
                que.append(0)
    return time