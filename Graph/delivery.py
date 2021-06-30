from collections import defaultdict
import heapq

def solution(N, road, K):
    answer = 0
    graph = defaultdict(dict)

    for (s, e, w) in road:
        try:
            graph[s][e] = min(w, graph[s][e])
            graph[e][s] = min(w, graph[e][s])
        except:
            graph[s][e] = w
            graph[e][s] = w

    def dijkstra(graph):
        distances = {node: float('inf') for node in graph}
        distances[1] = 0
        heap = []

        heapq.heappush(heap, [distances[1], 1])

        while heap:
            distance, pos = heapq.heappop(heap)

            if distances[pos] < distance:
                continue

            for arrival, distance2 in graph[pos].items():
                opt_distance = distance + distance2

                if opt_distance < distances[arrival]:
                    distances[arrival] = opt_distance
                    heapq.heappush(heap, [opt_distance, arrival])
        return distances

    for v in dijkstra(graph).values():
        if v <= K:
            answer += 1

    return answer