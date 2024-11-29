class DisjointSet:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        self.count = size
    
    def find(self, x):
        if self.root[x] == x:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.count -= 1
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
        
    def get_count(self):
        return self.count

class Solution:
    # the idea is to use ds as its best to solve the connectivity between nodes
    # for everyone to become friends, we can say that they all are connected to each other directly / indirectly
    # so every log we need to union them and check if the number of sets are 1 or not
    # if sets is only 1, we will return the timestamp immediately as it should be the earliest possible
    # the thing is the logs is not sorted, so we need to sort it first before we can union all them together
    # time complexity : O(N + M log M + Mα(N)), N = number of people, M = number of logs
    #   - sort : O(M log M)
    #   - create ds : O(N)
    #   - iterate over logs, and do union. the amortized time complexity of the entire process is O(Mα(N))
    # space complexity : O(N + M)
    #   - ds : O(N)
    #   - sort : O(M)
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        ds = DisjointSet(n)

        logs.sort(key=lambda x: x[0])

        for log in logs:
            ds.union(log[1], log[2])
            count = ds.get_count()
            if count == 1:
                return log[0]
        
        return -1
        pass

s = Solution()

logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
n = 6
result = s.earliestAcq(logs, n)
print(result)
assert result == 20190301

logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]]
n = 4
result = s.earliestAcq(logs, n)
print(result)
assert result == 3

logs = [[9,3,0],[0,2,1],[8,0,1],[1,3,2],[2,2,0],[3,3,1]]
n = 4
result = s.earliestAcq(logs, n)
print(result)
assert result == 2
