class Solution:
    # idea is very similar to course schedule 1 problem
    # but in this case, we need to return the order instead of to check whether we can finish all the course
    # the order can have many answers and we need to return 1 of them only
    # time complexity : O(V + E), V = # of vertex, E = # of edges
    # space complexity : O(V + E)
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        in_degree = [0 for i in range(numCourses)]
        adj = [[] for i in range(numCourses)]
        result = []

        for pr in prerequisites:
            in_degree[pr[0]] += 1
            adj[pr[1]].append(pr[0])
        
        queue = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
        
        while len(queue) > 0:
            val = queue.pop(0)
            result.append(val)

            for i in adj[val]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
        
        if len(result) != numCourses:
            return []
        
        return result

s = Solution()

numCourses = 2
prerequisites = [[1,0]]
result = s.findOrder(numCourses, prerequisites)
print(result)

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
result = s.findOrder(numCourses, prerequisites)
print(result)

numCourses = 1
prerequisites = []
result = s.findOrder(numCourses, prerequisites)
print(result)

