'''
non linear data structure consisting vertices and edges

types:
- undirected
- directed
- weighted : edge that connecting between nodes can have "cost"

terminologies:
- vertex : nodes
- edge : connection between 2 vertex
- path : sequence of vertex to go through from one vertex to another. Can be multiple path from 1 vertex to other


========================================================================================================
Disjoint Set / Union Find data structure : two set that not have anything common
- useful to address the connectivity between components in the network 
- track a set of elements partitioned into a number disjoint subsets
- solve graph partition problem

terminologies
- parent node : direct parent of a vertex / node
- root node : node without parent

important function:
- find function : to find which set for a given member / find the root of a node
- union function : find which set of element 'u' and which set of element 'v', if they're different set, combine both sets -> make their root node the same

s1 = {1,2,3,4}
s2 = {5,6,7,8}

find(4) = s1
find(8) = s2

union(4,8):
- find(4) = s1
- find(8) = s2
- s1 u s2 = s3 = {1,2,3,4,5,6,7,8}

union(1,5):
- find(1) = s3
- find(5) = s3
- since 1 and 5 is in the same set, there's a cycle

2 ways to impleent disjoint set:
- Quick find : find O(1), union O(n)
- Quick union: find O(n), union O(n)

optimiziation from quick union:
- union by rank : to make the tree more balance during union operation so the find operation will take less operation
                  We make decision based on the height of the tree, if the height of root_x bigger than height of root_y, then root_y should point to root_x
                  This is because if we do otherwise, the height will become bigger, hence the traverse cost is bigger
- path compression : optimization for find method, so the we won't do the same operations for all node. If 1 node already know the root, the children should know also
                     will end up in like quick find
========================

DFS (Depth First Search)
"given a graph, how can we find all its nodes (vertex), and how we can find all paths between two nodes ?"
- can explore all paths from the start node to all the nodes
- going as deep as possible
- usually use stack as we want to going back after going deep so we can move to the next one

DFS usage:
- traverse all nodes (vertext) in graph
- traverse all path between any two nodes in graph
=========================

BFS (Breadth First Search)

BFS usage = DFS usage

Most advantage:
- efficiently get the shortest path between two nodes where all edges are equal and positive weights
'''

class DisjointSetQuickFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
    pass

    def find(self, x):
        # time complexity : O(1)
        return self.root[x]
    
    def union(self, x, y):
        # time complexity : O(n)
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            for i in range(len(self.root)):
                if self.root[i] == root_y:
                    self.root[i] = root_x
    
    def is_same_set(self, x, y):
        return self.find(x) == self.find(y)

class DisjointSetQuickUnion:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        pass

    def find(self, x):
        while self.root[x] != x:
            x = self.root[x]
        
        return x
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.root[root_y] = root_x

class DisjointsetUnionRank:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        pass

    def find(self, x):
        # time complexity : O(log N) because the tree is more balanced so the traverse can be more efficient
        while self.root[x] != x:
            x = self.root[x]
        return x
    
    def union(self, x, y):
        # time complexity : O(log n) due to find operation
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_x] = root_y
                self.rank[root_y] += 1
            pass

class DisjointSetPathCompression:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        pass

    def find(self, x):
        while self.root[x] != x:
            x = self.root[x]
        
        return x
        pass

    def find_path_compression(self, x):
        # time complexity : O(log N)
        if self.root[x] == x:
            return x
        
        self.root[x] = self.find_path_compression(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.root[root_y] = root_x
        pass

class BreadthFirstSearch:
    pass

uf = DisjointSetPathCompression(6)

uf.union(4, 5)
uf.union(3, 5)
uf.union(2, 5)
uf.union(1, 5)
uf.union(0, 5)

print(uf.root)

print(uf.find_path_compression(0))
print(uf.root)
# print(uf.rank)

for i in range(6):
    print(uf.find(i))