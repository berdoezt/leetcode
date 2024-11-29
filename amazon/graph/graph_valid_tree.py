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
                self.root[root_y] = self.root[root_x]
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = self.root[root_y]
            else:
                self.root[root_x] = self.root[root_y]
                self.rank[root_y] += 1
            
            return True
        else:
            return False
    
    def get_count(self):
        return self.count

class Solution:
    # idea is valid tree is a graph that NOT contain cycle and should not have 2 different tree (2 root)
    # so we can utilize disjoint set
    # to detect cycle, we can simply check the root of two node. If it has same root, it should have cycle
    # to detect if there're two or more tree, we can check how many root are there. We initialize counter as size, and decrease it as we union
    # time complexity : O(N⋅α(N)), N : number of nodes
    # space complexity : O(n)
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        ds = DisjointSet(n)

        for edge in edges:
            if not ds.union(edge[0], edge[1]):
                return False
        

        if ds.get_count() != 1:
            return False
        
        return True
        pass

s = Solution()

n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]
assert s.validTree(n, edges) == True

n = 5
edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
assert s.validTree(n, edges) == False