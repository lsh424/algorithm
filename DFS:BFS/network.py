import collections

def solution(n, computers):
    answer = 0
    dic = collections.defaultdict(list)

    def BFS(graph, root):
        queue = collections.deque()
        visit = []

        queue.append(root)

        while queue:
            node = queue.popleft()

            if node not in visit:
                visit.append(node)
                queue.extend(graph[node])

        for key in visit:
            del dic[key]
        return 1

    for i in range(len(computers)):
        dic[i] = list(filter(lambda x: x != i and computers[i][x] == 1, range(n)))

    while dic:
        answer += BFS(dic, list(dic.keys())[0])

    return answer