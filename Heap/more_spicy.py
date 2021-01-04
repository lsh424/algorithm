import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    factor = heapq.heappop(scoville)

    while factor < K:
        if len(scoville) >= 1:
            factor2 = heapq.heappop(scoville)
            factor = factor + factor2 * 2
            heapq.heappush(scoville, factor)

            answer += 1
        else:
            answer = -1
            break

        factor = heapq.heappop(scoville)

    return answer