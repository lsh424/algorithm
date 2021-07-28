from collections import defaultdict

n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = defaultdict(list)
result = []
q = []

for _ in range(m):
    student1, student2 = map(int, input().split())
    graph[student1].append(student2)
    indegree[student2] += 1

for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    n = q.pop()
    result.append(str(n))

    for i in graph[n]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(" ".join(result))