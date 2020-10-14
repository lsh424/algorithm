import collections

def solution(priorities, location):
    queue = collections.deque(priorities)
    answer = 0

    while True:
        p = queue.popleft()
        location -= 1

        if queue and max(queue) > p:
            queue.append(p)
            if location == -1:
                location = len(queue) - 1
        else:
            answer += 1

        if location == -1:
            return answer