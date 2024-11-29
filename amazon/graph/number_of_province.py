class DisjointSet:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        self.count = size
    
    def find(self, x):
        # path compression
        if self.root[x] == x:
            return x
        
        self.root[x] = self.find(self.root[x])
        return self.root[x]
        pass

    def union(self, x, y):
        # union by rank
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            self.count -= 1
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = self.root[root_x]
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = self.root[root_y]
            else:
                self.root[root_x] = self.root[root_y]
                self.rank[root_y] += 1
        pass

    def get_count(self):
        return self.count
    pass

class Solution:
    # using DSU (disjoint set union)
    # idea is since this is to find how many sets are there, we can use disjoint set data structure
    # in here, we create array to store the relation of node and its parent / root
    # initially, all nodes are its own root
    # when we iterate, if we found the connection, we will union it together (make the root same between those nodes)
    # when try to union, if the root are different, meaning there will be less group sets
    # so we will decreased by 1
    # time complexity = O(n^2)
    # space complexity = O(n)

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)

        ds = DisjointSet(n)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    ds.union(i, j)

        return ds.get_count()

s = Solution()

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
result = s.findCircleNum(isConnected)
assert result == 2

isConnected = [[1,0,0],[0,1,0],[0,0,1]]
result = s.findCircleNum(isConnected)
assert result == 3

isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
result = s.findCircleNum(isConnected)
assert result == 1