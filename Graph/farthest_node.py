from collections import defaultdict
import heapq

def solution(n, edge):
    answer = 0
    graph = defaultdict(list)

    for (n1, n2) in edge:
        graph[n1].append(n2)
        graph[n2].append(n1)

    def dijkstra(graph, start):
        max_distance = 0
        distance = {n:float('inf') for n in graph}

        distance[start] = 0
        heap = []

        heapq.heappush(heap,[distance[start], start])

        while heap:
            distance1, pos = heapq.heappop(heap)

            if distance[pos] < distance1:
                continue

            for arrival in graph[pos]:
                opt_distance = distance1 + 1

                if opt_distance < distance[arrival]:
                    if opt_distance > max_distance:
                        max_distance = opt_distance
                    distance[arrival] = opt_distance
                    heapq.heappush(heap, [opt_distance, arrival])

        return (distance, max_distance)

    result, max_distance = dijkstra(graph, 1)

    for distance in result.values():
        if distance == max_distance:
            answer += 1

    return answer