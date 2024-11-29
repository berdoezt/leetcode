class DisjointSet:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
    
    def find(self, x):
        if self.root[x] == x:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = self.root[x]
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = self.root[root_y]
            else:
                self.root[root_x] = self.root[root_y]
                self.rank[root_y] += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        ds = DisjointSet(len(s))

        for pair in pairs:
            ds.union(pair[0], pair[1])
        pass

sol = Solution()

s = "dcab"
pairs = [[0,3],[1,2]]
result = sol.smallestStringWithSwaps(s, pairs)
print(result)
assert result == "bacd"

s = "dcab"
pairs = [[0,3],[1,2],[0,2]]
result = sol.smallestStringWithSwaps(s, pairs)
print(result)
assert result == "abcd"

s = "cba"
pairs = [[0,1],[1,2]]
result = sol.smallestStringWithSwaps(s, pairs)
print(result)
assert result == "abc"