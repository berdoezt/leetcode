# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2969/

class Solution:
    # idea is to do transpose and then swap the columns
    # to transpose, we need to traverse like the stairs so we can swap
    # *
    # * *
    # * * *
    # * * * *
    # time complexity = O(n^2) because we iterate twice for single element
    # space complexity = O(1)
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # transpose
        for i in range(len(matrix)):
            for j in range(i + 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # swap columns
        for i in range(len(matrix)):
            half = int(len(matrix) / 2)
            for j in range(half):
                matrix[i][j], matrix[i][len(matrix) - j - 1] = matrix[i][len(matrix) - j - 1], matrix[i][j]

s = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
s.rotate(matrix)
print(matrix)
assert matrix == [[7,4,1],[8,5,2],[9,6,3]]

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(matrix)
print(matrix)
assert matrix == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        

# 0 0
# 1 0
# 1 1
# 2 0
# 2 1
# 2 2