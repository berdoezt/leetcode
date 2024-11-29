class DisjointSet:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        self.count = size
    pass

    def find(self, x):
        # path compression
        if self.root[x] == x:
            return x
        
        self.root[x] = self.find(self.root[x])
        return self.root[x]
        pass

    def union(self, x, y):
        # union rank
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.count -= 1
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_x] = root_y
                self.rank[root_y] += 1
        pass
    
    def get_count(self):
        return self.count

class Solution:
    # the task is to find how many sets we have given the edges that connect between node / vertex
    # idea is to use DS as its best to tackle this kind of problem
    # we start by storing the node - root relation in array self.root and root's height
    # now we will merge / union the node
    # initially the node is its root itself
    # when we merge, meaning they will be become together, so we substract by 1
    # it means there will be no 2 groups, but become 1
    # we keep doing this until the end
    # time complexity : O(N⋅α(N)), N : number of nodes
    # space complexity : O(n), n = number of nodes
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        ds = DisjointSet(n)

        for edge in edges:
            ds.union(edge[0], edge[1])

        return ds.get_count()

s = Solution()

n = 5 
edges = [[0,1],[1,2],[3,4]]
result = s.countComponents(n, edges)
print(result)
assert result == 2

n = 5 
edges = [[0,1],[1,2],[2,3],[3,4]]
result = s.countComponents(n, edges)
print(result)
assert result == 1