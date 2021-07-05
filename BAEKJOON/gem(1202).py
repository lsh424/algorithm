import heapq
import sys

n, k = map(int, input().split())
gem_heap = []
bag_heap = []
answer = 0

for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    gem_heap.append((m, v))

for _ in range(k):
    bag_heap.append(int(sys.stdin.readline()))

heapq.heapify(gem_heap)
heapq.heapify(bag_heap)
candidates = []

for _ in range(k):
    m = heapq.heappop(bag_heap)

    while gem_heap and m >= gem_heap[0][0]:
        gem_m, v = heapq.heappop(gem_heap)
        heapq.heappush(candidates, -v)

    if candidates:
        answer -= heapq.heappop(candidates)
    elif not gem_heap:
        break

print(answer)