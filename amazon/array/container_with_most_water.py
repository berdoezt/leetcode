# https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2963/

class Solution:
    # brute force
    # check every range, if bigger than max, max = area
    # time complexity : O(n^2)
    # space complexity : O(1)
    def maxArea(self, height: list[int]) -> int:
        m = 0
        
        for i in range(len(height)):
            for j in range(i, len(height)):
                m = max(m, (j - i) * min(height[i], height[j]))
        
        return m

class Solution2:
    # 2 pointers i and j
    # i to the first, j to the last
    # since between two pointer we always calculate using the lowest between those 2, we should move the lowest
    # this is because it will be more beneficial in the future
    # time complexity : O(n)
    # space complexity : O(1)
    def maxArea(self, height: list[int]) -> int:
        m = 0
        
        i = 0
        j = len(height) - 1

        while i < j:
            m = max(m, (j - i) * min(height[i], height[j]))
            if height[j] < height[i]:
                j -= 1
            else:
                i += 1
        
        return m

s = Solution2()

height = [1,8,6,2,5,4,8,3,7]
result = s.maxArea(height)
print(result)
assert result == 49