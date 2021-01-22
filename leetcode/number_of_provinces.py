class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(0, len(isConnected))]
        s = set()

        def find(x):
            if (x == parent[x]):
                return x

            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x = find(x)
            y = find(y)

            if (x > y):
                parent[x] = y
            else:
                parent[y] = parent[x]

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    union(i, j)

        for i in range(len(isConnected)):
            s.add(find(i))

        return len(s)