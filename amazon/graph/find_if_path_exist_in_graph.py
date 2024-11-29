class DisjointSet:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
    
    def find(self, x):
        if self.root[x] == x:
            return x
        
        self.root[x] = self.find(self.root[x])
        return self.root[x]
        pass

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = self.root[root_x]
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = self.root[root_y]
            else:
                self.root[root_y] = self.root[root_x]
                self.rank[root_x] += 1
        pass

class Solution:
    # idea is to use simple DS. This is because for source and destination, if there's path to it, it should also means they're on the same group / sets
    # so we will do union nodes in edges variable, then check if source and destination have the same root
    # if yes, they should be in the same sets, hence connected. Otherwise, they're not connected
    # time complexity : O(m⋅α(n)), m = # of edges, n = # of nodes
    # space complexity : O(n)
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:

        ds = DisjointSet(n)

        for edge in edges:
            ds.union(edge[0], edge[1])
        
        return ds.find(source) == ds.find(destination)
        pass

class Solution2:
    # dfs using stack iterative
    # idea is to create adjacency list to see the connected nodes (neighbours) from the current node for all node
    # to check if destination is reachable from source, we will start from source and put it in the stack
    # everytime we pop out the node, we will put the neighbours on the stack
    # to prevent it to going back to current node, we keep track of its node wether its already visited or not
    # if we found the destination, we return True no matter from which way
    # time complexity : O(V + E), V = # of vertex, E = # of edges
    # space complexity : O(V + E), V = # of vertex, E = # of edges
    #   - adjacency_list : V + E
    #   - stack : V
    #   - visited : V
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adjacency_list = {}

        for edge in edges:
            if edge[0] not in adjacency_list:
                adjacency_list[edge[0]] = [edge[1]]
            else:
                adjacency_list[edge[0]].append(edge[1])
            
            if edge[1] not in adjacency_list:
                adjacency_list[edge[1]] = [edge[0]]
            else:
                adjacency_list[edge[1]].append(edge[0])
        
        stack = [source]
        visited = {source: True}

        while len(stack) > 0:
            val = stack.pop()
            if val == destination:
                return True
            
            for i in adjacency_list[val]:
                if i not in visited:
                    visited[i] = True
                    stack.append(i)
        
        return False

            
        pass

s = Solution2()

n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
assert s.validPath(n, edges, source, destination) == True

n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5
assert s.validPath(n, edges, source, destination) == False