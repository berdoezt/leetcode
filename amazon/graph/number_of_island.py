class DisjointSet:
    def __init__(self, coordinate: list):
        self.root = {}
        self.rank = {}

        for i in coordinate:
            self.root[i] = i
            self.rank[i] = 1

        self.count = len(coordinate)
    
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
                self.root[root_y] = self.root[root_x]
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = self.root[root_y]
            else:
                self.root[root_x] = self.root[root_y]
                self.rank[root_y] += 1
            pass
        pass
    
    def get_count(self):
        return self.count
    pass

class Solution:
    # idea is to use disjoint set
    # we can use disjoint set because basically the question is to ask about how many sets are there
    # we can think the island as set
    # the "1" will form an island, and if it connected to other "1" horizontal / vertical, it means they're the same island
    # in this case we can say its the same set
    # so now its simple. We need to put the location of "1" in the self.root. We are using map here
    # when we traverse, everytime we found "1", we want to check with the neighbours, if they're also "1", we will union them together
    # after union it, we can mark current node as "0". This to make sure when we are visiting other location, this location will not be calculated again as its already calculated before
    # time complexity : O(m x n)
    # space complexity : O(m x n)
    def numIslands(self, grid: list[list[str]]) -> int:

        coordinate_one = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    coordinate_one.append("{}-{}".format(i, j))
        
        ds = DisjointSet(coordinate_one)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    if i - 1 >= 0 and grid[i - 1][j] == "1":
                        ds.union("{}-{}".format(i, j), "{}-{}".format(i-1, j))
                    
                    if i + 1 <= len(grid) - 1 and grid[i + 1][j] == "1":
                        ds.union("{}-{}".format(i, j), "{}-{}".format(i+1, j))
                    
                    if j - 1 >= 0 and grid[i][j - 1] == "1":
                        ds.union("{}-{}".format(i, j), "{}-{}".format(i, j-1))
                    
                    if j + 1 <= len(grid[i]) - 1 and grid[i][j + 1] == "1":
                        ds.union("{}-{}".format(i, j), "{}-{}".format(i,j+1))
                    pass
        
        return ds.get_count()

s = Solution()

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
result = s.numIslands(grid)
print(result)
assert result == 1

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
result = s.numIslands(grid)
print(result)
assert result == 3

grid = [
  ["1","1","1","1","1"],
  ["1","1","1","1","1"],
  ["1","1","1","1","1"],
  ["1","1","1","1","1"]
]
result = s.numIslands(grid)
print(result)
assert result == 1


grid = [
    ["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
    ["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
    ["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
    ["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
    ["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]
]

result = s.numIslands(grid)
print(result)
assert result == 1