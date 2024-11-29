'''
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        right = True
        left = False
        up = False
        down = False

        i = 0
        j = 0
        m = len(matrix)
        n = len(matrix[0])

        left_boarder = 0
        up_boarder = 1
        count = m * n
        result = []

        while True:
            if count == 0:
                break
            result.append(matrix[i][j])
            count -= 1

            if right:
                j += 1
                if j == n:
                    j -= 1
                    i += 1
                    right = False
                    down = True
                    n -= 1
                pass
            elif down:
                i += 1
                if i == m:
                    i -= 1
                    j -= 1
                    down = False
                    left = True
                    m -= 1
                pass
            elif left:
                j -= 1
                if j < left_boarder:
                    j += 1
                    i -= 1
                    left = False
                    up = True
                    left_boarder += 1
                pass
            elif up:
                i -= 1
                if i < up_boarder:
                    i += 1
                    j += 1
                    up = False
                    right = True
                    up_boarder += 1
                pass
        
        return result

sol = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = sol.spiralOrder(matrix)
assert result == [1,2,3,6,9,8,7,4,5]

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
result = sol.spiralOrder(matrix)
assert result == [1,2,3,4,8,12,11,10,9,5,6,7]