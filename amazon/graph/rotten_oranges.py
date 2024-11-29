# https://leetcode.com/problems/rotting-oranges/description/

class Solution:
    # idea is to use BFS, because it will rotting the 4 directional (up, down, left, right) and we need to find the minimum time of it
    # BFS is great and the answer.
    # the rotten orange can be place multiple places inside the 2D matrix
    # so we can use it as our starting point
    # we will calculate the number of fresh orange at first, and subtract by 1 whenever we are rotting it. If at the end the total of fresh orange is > 0, means there's still unreachable fresh orange and we return -1
    # we put all the rottent orange coordinate in our queue as starting point. 
    # To calculate the time, we put this data into the queue -> [i, j, time]
    # this way, we can know from what time this data come, and calculate the maximum time. Remember with BFS, we get the minimum time to do it. But we get the maximum time because there's possibility where there're multiple starting point
    # hence, there will case in our iteration where we get the "past" time. So to keep track of it, we put time into the array that push to the queue
    # now, we will check the 4 directional (up, down, left, right) if there's fresh orange (1). If there is, we mark it as rotten (2) so it won't process again, and decrease the total_fresh_orange by 1, then increase the time
    # time complexity : O(M * N), M : grid row, N: col row
    # space complexity : O(M * N)
    def orangesRotting(self, grid: list[list[int]]) -> int:
        count_fresh = 0
        queue = []
        time = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count_fresh += 1
                
                if grid[i][j] == 2:
                    queue.append([i,j,time])
        
        while len(queue) > 0:
            v = queue.pop(0)

            i = v[0]
            j = v[1]
            t = v[2]

            if i - 1 >= 0:
                if grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    count_fresh -= 1
                    time = max(time, t + 1)
                    queue.append([i - 1,j, t + 1])

            if i + 1 < len(grid):
                if grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    count_fresh -= 1
                    time = max(time, t + 1)
                    queue.append([i + 1,j, t + 1])
            
            if j + 1 < len(grid[0]):
                if grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    count_fresh -= 1
                    time = max(time, t + 1)
                    queue.append([i,j + 1, t + 1])
            
            if j - 1 >= 0:
                if grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    count_fresh -= 1
                    time = max(time, t + 1)
                    queue.append([i,j - 1, t + 1])

        if count_fresh > 0:
            return -1
        
        return time

s = Solution()

grid = [[2,1,1],[1,1,0],[0,1,1]]
result = s.orangesRotting(grid)
print(result)
assert result == 4

grid = grid = [[2,1,1],[0,1,1],[1,0,1]]
result = s.orangesRotting(grid)
print(result)
assert result == -1