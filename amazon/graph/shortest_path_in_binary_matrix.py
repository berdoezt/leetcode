class Solution:
    # idea is since we are asked to find the shortest path between source and target and need to avoid obstacles, we can utilize BFS
    # BFS is guarantee to get the shortest one when we encounter the target in the first time. This is the nature of BFS, the breadth
    # so when we get to the next node, we keep track of the number of nodes
    # in the queue we store the coordinate and the number of nodes so far
    # time complexity : O(n^2)
    # space complexity : O(n^2)
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        n = len(grid)
        source = [0,0,1]
        target = [n-1,n-1]
        visited = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(False)
            visited.append(temp)

        queue = [source]
        visited[0][0] = True

        while len(queue) > 0:
            val = queue.pop(0)

            i = val[0]
            j = val[1]
            c = val[2]

            if i == target[0] and j == target[1]:
                return c

            if i - 1 >= 0 and grid[i-1][j] == 0 and visited[i-1][j] == False:
                visited[i-1][j] = True
                queue.append([i-1,j,c+1])
            
            if i + 1 < n and grid[i+1][j] == 0 and visited[i+1][j] == False:
                visited[i+1][j] = True
                queue.append([i+1,j,c+1])
            
            if j - 1 >= 0 and grid[i][j-1] == 0 and visited[i][j-1] == False:
                visited[i][j-1] = True
                queue.append([i,j-1,c+1])
            
            if j + 1 < n and grid[i][j+1] == 0 and visited[i][j+1] == False:
                visited[i][j+1] = True
                queue.append([i,j+1,c+1])
            
            if i - 1 >= 0 and j - 1 >= 0 and grid[i-1][j-1] == 0 and visited[i-1][j-1] == False:
                visited[i-1][j-1] = True
                queue.append([i-1,j-1,c+1])
            
            if i - 1 >= 0 and j + 1 < n and grid[i-1][j+1] == 0 and visited[i-1][j+1] == False:
                visited[i-1][j+1] = True
                queue.append([i-1,j+1,c+1])
            
            if i + 1 < n and j + 1 < n and grid[i+1][j+1] == 0 and visited[i+1][j+1] == False:
                visited[i+1][j+1] = True
                queue.append([i+1,j+1,c+1])
            
            if i + 1 < n and j - 1 >= 0 and grid[i+1][j-1] == 0 and visited[i+1][j-1] == False:
                visited[i+1][j-1] = True
                queue.append([i+1,j-1,c+1])

        return -1
        pass

s = Solution()

grid = [[0,0,0],[1,1,0],[1,1,0]]
result = s.shortestPathBinaryMatrix(grid)
print(result)
assert result == 4

grid = [[1,0,0],[1,1,0],[1,1,0]]
result = s.shortestPathBinaryMatrix(grid)
print(result)
assert result == -1

grid = [[0,0,0],[1,1,0],[1,0,1]]
result = s.shortestPathBinaryMatrix(grid)
print(result)
assert result == -1