class Solution:
    # this is the problem of topological sort using kahn's algorithm
    # each node form a chain of pre-requisite where one node need to done first before we can traverse to the next node
    # so idea is to have in_degree data of every node. In_degree means number of arrow that's coming to that node
    # we will use queue to keep track the node with in_degree = 0
    # when we process a node, we check its neighbour and decrease neighbour's degree
    # whenever a node have in_degree = 0, means it can be processed because there's no more pre requisite needed to take that node
    # hence we put in the queue
    # when we pop the value out of the queue, we increase the counter
    # ideally, if no cyclic, the counter would be the total number of node (courses)
    # this is because at the end, all nodes would have in_degree = 0
    # otherwise, it means there's still node with in_degree not 0, and 1 possibility is because it has cycle
    # time complexity : O(V + E), V = # of vertex, E = # of edge
    # space complexity : O(V + E)
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        degree = [0 for i in range(numCourses)]
        adj = [[] for i in range(numCourses)]

        for pr in prerequisites:
            if pr[0] == pr[1]:
                return False
            
            degree[pr[0]] += 1
            adj[pr[1]].append(pr[0])
        
        queue = []

        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
        
        if len(queue) == 0:
            return False
        
        counter = 0
        while len(queue) > 0:
            val = queue.pop(0)
            counter += 1
            for i in adj[val]:
                if degree[i] == 0:
                    return False
                
                degree[i] -= 1
                if degree[i] == 0:
                    queue.append(i)
        
        return counter == numCourses
        pass

s = Solution()

numCourses = 2
prerequisites = [[1,0]]
assert s.canFinish(numCourses, prerequisites) == True

numCourses = 2
prerequisites = [[1,0],[0,1]]
assert s.canFinish(numCourses, prerequisites) == False

numCourses = 20
prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
assert s.canFinish(numCourses, prerequisites) == False