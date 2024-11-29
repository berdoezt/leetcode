class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        adjacency_list = {}

        for i in range(len(graph)):
            for j in graph[i]:
                if i not in adjacency_list:
                    adjacency_list[i] = [j]
                else:
                    adjacency_list[i].append(j)
        
        source = 0
        destination = len(graph) - 1

        stack = [source]
        visited = {source: True}

        result = []

        while len(stack) > 0:
            val = stack.pop()
            
            pass

        return result



0 : 1, 2
1: 3
2: 3


s = Solution()

graph = [[1,2],[3],[3],[]]
s.allPathsSourceTarget(graph)