# 어려움;; 다른사람 코드 참고

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse = True)

        h = []
        res = d = 0
        while events or h:
            if not h:
                d = events[-1][0] # 마지막 인덱스의 시작 시간
            while events and events[-1][0] <= d: #
                heapq.heappush(h, events.pop()[1]) # 힙에 마지막 요소 끝나는 시간 넣기

            heapq.heappop(h) # 꺼내기
            res += 1

            d += 1

            while h and h[0] < d:
                heapq.heappop(h)
        return res